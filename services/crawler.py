import requests
from bs4 import BeautifulSoup

def get_page(url: str):

    r = requests.get(url, timeout=10)

    soup = BeautifulSoup(r.text, "html.parser")

    title = soup.title.text if soup.title else ""

    meta_desc = ""
    meta = soup.find("meta", {"name":"description"})
    if meta:
        meta_desc = meta.get("content","")

    text = soup.get_text()

    return {
        "html": r.text,
        "text": text,
        "title": title,
        "description": meta_desc
    }