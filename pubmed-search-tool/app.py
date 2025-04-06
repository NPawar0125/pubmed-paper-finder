import streamlit as st
from pubmed_fetcher.fetch import search_pubmed, fetch_pubmed_details

st.set_page_config(page_title="PubMed Search", layout="wide")

st.title("🔬 PubMed Paper Finder")

query = st.text_input("Enter your PubMed query", value="cancer therapy")

if st.button("Search"):
    with st.spinner("Searching PubMed..."):
        pmids = search_pubmed(query)
        results = fetch_pubmed_details(pmids)

    if results:
        for paper in results:
            st.markdown("### 📝 " + paper["Title"])
            st.write(f"**PubmedID:** {paper['PubmedID']}")
            st.write(f"**Publication Date:** {paper['Publication Date']}")
            st.write(f"**Non-academic Author(s):** {paper.get('Non-academic Author(s)', '-')}")
            st.write(f"**Company Affiliation(s):** {paper.get('Company Affiliation(s)', '-')}")
            st.write(f"**Corresponding Author Email:** {paper.get('Corresponding Author Email', '-')}")
            st.markdown("---")
    else:
        st.warning("No results found.")
