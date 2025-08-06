from googlesearch import search

def get_company_urls(query, num_results=10):
    return list(search(query, num_results=num_results))

def get_competitors(company_name, num_results=3):
    try:
        query = f"{company_name} competitors"
        return list(search(query, num_results=num_results))
    except Exception as e:
        return [f"Error: {e}"]

