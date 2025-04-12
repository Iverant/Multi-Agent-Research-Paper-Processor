import requests

def search_semantic_scholar(query, limit=10):
    url = "https://api.semanticscholar.org/graph/v1/paper/search"
    params = {
        "query": query,
        "limit": limit,
        "fields": "title,url,openAccessPdf"
    }

    response = requests.get(url, params=params)
    data = response.json()
    
    results = []
    for paper in data.get("data", []):
        print("entered loop")
        pdf_url = paper.get("openAccessPdf", {}).get("url")
        results.append({
            "title": paper.get("title"),
            "semanticscholar_url": paper.get("url"),
            "pdf_url": pdf_url
        })

    return results


