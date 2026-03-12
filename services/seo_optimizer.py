from bs4 import BeautifulSoup

def analyze_seo(html):

    soup = BeautifulSoup(html,"html.parser")

    issues = []

    if not soup.title:
        issues.append("Отсутствует title")

    if not soup.find("meta", {"name":"description"}):
        issues.append("Нет meta description")

    h1 = soup.find_all("h1")

    if len(h1) == 0:
        issues.append("Нет H1")

    if len(h1) > 1:
        issues.append("Слишком много H1")

    return issues