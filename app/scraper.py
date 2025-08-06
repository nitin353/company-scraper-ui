from app.search_scraper import get_company_urls, get_competitors
from app.site_scraper import scrape_company_info

def run_scraper(query, num_results=5):
    urls = get_company_urls(query, num_results=num_results)
    results = []

    for url in urls:
        info = scrape_company_info(url)
        if "company_name" in info and info["company_name"] != "N/A":
            competitors = get_competitors(info["company_name"], num_results=3)
            info["competitors"] = competitors
        else:
            info["competitors"] = []
        results.append(info)

    return results
