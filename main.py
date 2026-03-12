from fastapi import FastAPI
from api.routes_analysis import router as analysis_router
from api.routes_content import router as content_router
from api.routes_knowledge import router as knowledge_router
from api.routes_visualization import router as viz_router

app = FastAPI(title="SEO AI Optimizer")

app.include_router(analysis_router)
app.include_router(content_router)
app.include_router(knowledge_router)
app.include_router(viz_router)