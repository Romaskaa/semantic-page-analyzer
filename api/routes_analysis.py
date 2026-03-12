from fastapi import APIRouter
from services.crawler import get_page
from services.text_cleaner import clean_text
from services.semantic_core import extract_keywords
from services.clustering import cluster_keywords
from services.seo_optimizer import analyze_seo
from services.error_analyzer import estimate_improvement
from services.jsonld_generator import generate_jsonld

router = APIRouter()

@router.get("/analyze")
def analyze(url: str):
    page = get_page(url)

    words = clean_text(page["text"])
    keywords_list = extract_keywords(words)
    keywords_only = [k[0] for k in keywords_list]

    clusters = cluster_keywords(keywords_list)

    issues = analyze_seo(page["html"])
    seo_score = estimate_improvement(issues)

    title = page.get("title", "Default Title")
    description = page.get("meta_description", "Default Description")
    author = page.get("author", "Default Author")
    published_date = page.get("published_date", "Default Published Date")

    jsonld = generate_jsonld(title, description, keywords_only, author, published_date)

    return {
        "clusters": clusters,
        "issues": issues,
        "seo_score": seo_score,
        "jsonld": jsonld
    }