from fastapi import APIRouter
from utils.charts import plot_seo_report
from services.seo_optimizer import analyze_seo
from services.crawler import get_page

router = APIRouter()

@router.get("/seo-chart")
def chart(url: str):
    page = get_page(url)
    html = page["html"]

    seo_report = analyze_seo(html, url)

    path = plot_seo_report(seo_report)
    return {"chart": path}