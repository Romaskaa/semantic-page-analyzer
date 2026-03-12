from bs4 import BeautifulSoup
from urllib.parse import urlparse

def analyze_seo(html, url):

    soup = BeautifulSoup(html, "html.parser")

    issues = []
    warnings = []
    passed = []

    parsed = urlparse(url)
    domain = parsed.netloc

    title = soup.title.string.strip() if soup.title and soup.title.string else ""

    if not title:
        issues.append("Отсутствует title")

    elif len(title) < 30:
        warnings.append("Title слишком короткий")

    elif len(title) > 60:
        warnings.append("Title слишком длинный")

    else:
        passed.append("Title оптимален")

    desc_tag = soup.find("meta", {"name": "description"})

    if not desc_tag:
        issues.append("Нет meta description")

    else:

        desc = desc_tag.get("content", "")

        if len(desc) < 120:
            warnings.append("Description слишком короткий")

        elif len(desc) > 160:
            warnings.append("Description слишком длинный")

        else:
            passed.append("Description оптимален")

    robots = soup.find("meta", {"name": "robots"})

    if robots:
        passed.append("Meta robots найден")

    else:
        warnings.append("Meta robots отсутствует")

    canonical = soup.find("link", {"rel": "canonical"})

    if canonical:
        passed.append("Canonical присутствует")

    else:
        warnings.append("Нет canonical")

    h1_tags = soup.find_all("h1")

    if len(h1_tags) == 0:
        issues.append("Нет H1")

    elif len(h1_tags) > 1:
        warnings.append("Больше одного H1")

    else:
        passed.append("H1 присутствует")

    h2_tags = soup.find_all("h2")

    if len(h2_tags) < 2:
        warnings.append("Мало H2")

    else:
        passed.append("H2 присутствуют")

    h3_tags = soup.find_all("h3")

    if len(h3_tags) == 0:
        warnings.append("Нет H3")

    text = soup.get_text(separator=" ")
    words = text.split()
    word_count = len(words)

    if word_count < 300:
        issues.append("Слишком мало текста (<300 слов)")

    elif word_count < 600:
        warnings.append("Желательно больше текста")

    else:
        passed.append("Достаточно текста")

    images = soup.find_all("img")

    if not images:
        warnings.append("Нет изображений")

    images_without_alt = []

    for img in images:

        if not img.get("alt"):
            images_without_alt.append(img)

    if images_without_alt:
        warnings.append(f"{len(images_without_alt)} изображений без alt")

    else:
        if images:
            passed.append("Все изображения имеют alt")

    links = soup.find_all("a")

    internal_links = []
    external_links = []

    for link in links:

        href = link.get("href")

        if not href:
            continue

        if href.startswith("http"):

            if domain in href:
                internal_links.append(href)

            else:
                external_links.append(href)

        else:
            internal_links.append(href)

    if len(internal_links) == 0:
        warnings.append("Нет внутренних ссылок")

    else:
        passed.append("Есть внутренние ссылки")

    if len(external_links) == 0:
        warnings.append("Нет внешних ссылок")

    schema = soup.find("script", {"type": "application/ld+json"})

    if schema:
        passed.append("Schema.org присутствует")

    else:
        warnings.append("Нет Schema.org")

    og_title = soup.find("meta", {"property": "og:title"})
    og_desc = soup.find("meta", {"property": "og:description"})
    og_image = soup.find("meta", {"property": "og:image"})

    if og_title and og_desc and og_image:
        passed.append("OpenGraph настроен")

    else:
        warnings.append("OpenGraph настроен не полностью")

    twitter_card = soup.find("meta", {"name": "twitter:card"})

    if twitter_card:
        passed.append("Twitter card найден")

    else:
        warnings.append("Twitter card отсутствует")

    viewport = soup.find("meta", {"name": "viewport"})

    if viewport:
        passed.append("Viewport присутствует")

    else:
        issues.append("Нет viewport (плохая мобильная оптимизация)")

    html_tag = soup.find("html")

    if html_tag and html_tag.get("lang"):
        passed.append("Язык страницы указан")

    else:
        warnings.append("Не указан lang")

    favicon = soup.find("link", rel="icon")

    if favicon:
        passed.append("Favicon найден")

    else:
        warnings.append("Нет favicon")

    tables = soup.find_all("table")

    if tables:
        passed.append("Таблицы присутствуют")

    lists = soup.find_all(["ul", "ol"])

    if lists:
        passed.append("Списки присутствуют")

    buttons = soup.find_all("button")

    if buttons:
        passed.append("Есть кнопки")

    iframes = soup.find_all("iframe")

    if iframes:
        warnings.append("Есть iframe — возможное замедление страницы")

    scripts = soup.find_all("script")

    if len(scripts) > 20:
        warnings.append("Слишком много JS скриптов")

    return {
        "issues": issues,
        "warnings": warnings,
        "passed": passed
    }