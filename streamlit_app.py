import streamlit as st
import pandas as pd
import json
from app.scraper import run_scraper

st.set_page_config(page_title="Company Info Scraper", layout="wide")
st.title("🔍 Company Info Scraper")

query = st.text_input("Enter search query", placeholder="e.g., AI startups in India")
num_results = st.slider("Number of companies to scrape", 1, 20, 5)

if st.button("Start Scraping"):
    if not query.strip():
        st.error("❌ Please enter a search query.")
    else:
        with st.spinner("Scraping in progress..."):
            data = run_scraper(query, num_results)

        if data:
            df = pd.DataFrame(data)
            st.success(f"✅ Scraped {len(df)} companies.")
            st.dataframe(df)

            # Downloads
            json_data = json.dumps(data, indent=2)
            csv_data = df.to_csv(index=False)

            st.download_button("⬇️ Download JSON", json_data, file_name="companies.json", mime="application/json")
            st.download_button("⬇️ Download CSV", csv_data, file_name="companies.csv", mime="text/csv")
        else:
            st.warning("No results found or failed to scrape.")
