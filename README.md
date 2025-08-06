# 🔍 Company Info Scraper Tool

This is a Python-based web scraping tool that takes a search query, extracts company URLs using Google Search, and scrapes each site for valuable information such as:

- Company name
- Website URL
- Contact emails and phone numbers
- Technology stack (e.g., React, Django, AWS, etc.)
- Competitor links (via additional Google searches)

---

## ✅ Features & Extraction Capabilities

| Feature             | Description |
|---------------------|-------------|
| 🌐 **Google Search Integration** | Uses `googlesearch-python` to find company websites based on your query. |
| 🏢 **Company Info Extraction** | Extracts data like company name, emails, and phone numbers from the site. |
| 🧰 **Tech Stack Detection** | Detects common technologies from the website HTML (React, Node.js, Django, etc.). |
| 🤝 **Competitor Discovery** | Performs a secondary search for each company to list competitor URLs. |
| 🗃 **Output Format** | Saves results in both JSON (`output/companies.json`) and CSV (`output/companies.csv`). |

---

## 🚀 Setup & Execution Instructions

### 🔧 Prerequisites

- Python 3.9 or higher
- Internet connection

### 📦 Step 1: Install Dependencies

```bash
pip install -r requirements.txt
```

### 🏁 Step 2: Run the Script

```bash
python main.py
```

### 💬 Step 3: Enter a Search Query

Example:
```
AI startups in India
```

---

## 📂 Output Files

After running, you'll find:

- `output/companies.json` – structured output in JSON format
- `output/companies.csv` – data saved as a spreadsheet for easy viewing

---

## 🧠 Design Decisions & Assumptions

- **Search Engine-Based Discovery**: We use Google Search (via `googlesearch-python`) instead of a paid API like Crunchbase.
- **Basic Tech Stack Matching**: Looks for predefined tech terms in HTML (no JS rendering or headless browser).
- **Random Delay Added**: Between requests to avoid hitting servers too quickly and reduce the chance of getting blocked.
- **Competitor Info**: Basic search for `"Company Name competitors"` assumes top search results are valid references.
- **Robust Output**: If any scraping fails, the tool records the error but continues running.

---

## 📁 Project Structure

```
webscraper/
├── main.py
├── search_scraper.py
├── site_scraper.py
├── requirements.txt
├── README.md
└── output/
    ├── companies.json
    └── companies.csv
```

---

## 🙌 Author & Credits

Built by [Your Name] for educational and research purposes.  
Uses open libraries: `requests`, `beautifulsoup4`, `googlesearch-python`, `pandas`.
