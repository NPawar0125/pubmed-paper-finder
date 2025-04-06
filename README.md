# pubmed-search-tool

PubMed Paper Finder is a command-line and interactive tool that searches PubMed using full query syntax and identifies research papers with at least one author affiliated with a pharmaceutical or biotech company. Results can be exported to CSV or viewed interactively via a Streamlit web app.

# PubMed Paper Fetcher 🧬

A command-line and interactive Streamlit-based tool to search PubMed, identify papers with non-academic (biotech/pharma) affiliations, and export results to CSV.


## 🔍 Features

- ✅ Full support for [PubMed’s query syntax](https://pubmed.ncbi.nlm.nih.gov/advanced/)
- ✅ Identifies authors affiliated with pharmaceutical or biotech companies using heuristics
- ✅ Outputs results in CSV with:
  - PubMed ID
  - Title
  - Publication Date
  - Non-academic Author(s)
  - Company Affiliation(s)
  - Corresponding Author Email
- ✅ Command-line and Web UI (Streamlit) interface
- ✅ Debug mode for transparency and development
- ✅ Modular Python code with type hints and clear organization



🔹 Usage
  - Command-Line Interface
   - python3 cli.py "your query here"
   - Available options:
     - --debug - Print detailed debug output
     - --file filename.csv - Save results as a CSV file
     - --help - Show usage instructions


🔹 Interactive UI (Streamlit)
  - python3 -m streamlit run app.py
  - Then open http://localhost:8501 in your browser.


🔹 Project Structure
  - pubmed-paper-fetcher/pubmed-search-tool/
  - ├── cli.py                      # Command-line interface
  - ├── app.py                      # Streamlit UI
  - ├── pubmed_fetcher/
  - │   └── fetch.py                # Main fetching logic (modular)
  - ├── requirements.txt            # Dependencies
  - └── README.md                   # Project documentation

📌 Tools Used
- Entrez E-Utilities (NCBI)
- xml.etree.ElementTree for parsing
- Streamlit for the web interface
- argparse for CLI


Author
- Made with ❤️ 
- GitHub: @Npawar0125
