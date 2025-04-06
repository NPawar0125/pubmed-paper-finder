import argparse
import csv
from pubmed_fetcher.fetch import search_pubmed, fetch_pubmed_details
from typing import Optional


def save_to_csv(data: list[dict], filename: str) -> None:
    """Save the fetched data to a CSV file."""
    if not data:
        print("No results to save.")
        return

    with open(filename, mode='w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=data[0].keys())
        writer.writeheader()
        writer.writerows(data)

def main():
    parser = argparse.ArgumentParser(description="Fetch PubMed papers matching a query.")

    parser.add_argument("query", help="Search query for PubMed")
    parser.add_argument("-f", "--file", help="Filename to save the output CSV")
    parser.add_argument("-d", "--debug", action="store_true", help="Enable debug output")

    args = parser.parse_args()

    if args.debug:
        print(f"Searching PubMed for: {args.query}")

    pmids = search_pubmed(args.query, max_results=20)
    results = fetch_pubmed_details(pmids)

    if not results:
        print("No company-affiliated papers found.")
    elif args.file:
        save_to_csv(results, args.file)
        print(f"Results saved to {args.file}")
    else:
        for item in results:
            print(f"PubmedID: {item['PubmedID']}")
            print(f"Title: {item['Title']}")
            print(f"Publication Date: {item['Publication Date']}")
            print(f"Non-academic Author(s): {item['Non-academic Author(s)']}")
            print(f"Company Affiliation(s): {item['Company Affiliation(s)']}")
            print(f"Corresponding Author Email: {item['Corresponding Author Email']}")
            print("-" * 40)

if __name__ == "__main__":
    main()
