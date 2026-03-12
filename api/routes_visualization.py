from fastapi import APIRouter
from utils.charts import plot_seo_score

router = APIRouter()

@router.get("/seo-chart")

def chart(score:int):

    path = plot_seo_score(score)

    return {"chart":path}