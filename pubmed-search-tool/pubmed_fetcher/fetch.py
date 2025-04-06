# pubmed_fetcher/fetch.py

from typing import List, Dict
import requests
import xml.etree.ElementTree as ET

def is_non_academic(affiliation: str) -> bool:
    academic_keywords = ["university", "institute", "college", "school", "department", "hospital", "center"]
    return not any(word in affiliation.lower() for word in academic_keywords)

def search_pubmed(query: str, max_results: int = 20) -> List[str]:
    """Search PubMed and return a list of PubMed IDs."""
    base_url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi"
    params = {
        "db": "pubmed",
        "term": query,
        "retmode": "json",
        "retmax": max_results
    }
    response = requests.get(base_url, params=params)
    response.raise_for_status()
    data = response.json()
    return data["esearchresult"]["idlist"]

def fetch_pubmed_details(pmids: List[str]) -> List[Dict[str, str]]:
    if not pmids:
        return []

    base_url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi"
    params = {
        "db": "pubmed",
        "id": ",".join(pmids),
        "retmode": "xml"
    }
    response = requests.get(base_url, params=params)
    response.raise_for_status()

    root = ET.fromstring(response.content)
    results = []

    for article in root.findall(".//PubmedArticle"):
        pmid = article.findtext(".//PMID") or "N/A"
        title = article.findtext(".//ArticleTitle") or "N/A"
        pub_date_elem = article.find(".//PubDate")
        pub_year = pub_date_elem.findtext("Year") if pub_date_elem is not None else "Unknown"

        non_academic_authors = []
        companies = set()
        corresponding_email = None

        author_list = article.findall(".//AuthorList/Author")
        for author in author_list:
            last = author.findtext("LastName") or ""
            first = author.findtext("ForeName") or ""
            full_name = f"{first} {last}".strip()

            aff_info = author.find("AffiliationInfo")
            if aff_info is not None:
                affiliation = aff_info.findtext("Affiliation") or ""

                if "@" in affiliation and corresponding_email is None:
                    # Try to extract email
                    tokens = affiliation.split()
                    corresponding_email = next((t for t in tokens if "@" in t), None)

                if is_non_academic(affiliation):
                    companies.add(affiliation)
                    if full_name:
                        non_academic_authors.append(full_name)

        if companies:
            results.append({
                "PubmedID": pmid,
                "Title": title,
                "Publication Date": pub_year,
                "Non-academic Author(s)": "; ".join(non_academic_authors) or "N/A",
                "Company Affiliation(s)": "; ".join(companies) or "N/A",
                "Corresponding Author Email": corresponding_email or "N/A"
            })

    return results
