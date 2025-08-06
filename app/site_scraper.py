import requests
from bs4 import BeautifulSoup
import re
import random
import time

TECH_KEYWORDS = [
    "React", "Angular", "Vue", "Node.js", "Django", "Flask",
    "Laravel", "Spring", "AWS", "Azure", "Firebase", "Tailwind", "Bootstrap"
]

def get_tech_stack(html_text):
    return [tech for tech in TECH_KEYWORDS if tech.lower() in html_text.lower()]

def scrape_company_info(url):
    try:
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
        }
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')

        title = soup.title.string.strip() if soup.title else "N/A"
        emails = list(set(re.findall(r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+", response.text)))
        phones = list(set(re.findall(r'\+?\d[\d\s\-\(\)]{8,}\d', response.text)))
        tech_stack = get_tech_stack(response.text)

        time.sleep(random.uniform(2, 3.5))

        return {
            "company_name": title,
            "website": url,
            "emails": emails,
            "phone_numbers": phones,
            "tech_stack": tech_stack
        }

    except requests.exceptions.RequestException as e:
        return {
            "website": url,
            "company_name": "N/A",
            "emails": [],
            "phone_numbers": [],
            "tech_stack": [],
            "error": str(e)
        }
