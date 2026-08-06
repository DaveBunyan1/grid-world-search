from fastapi import FastAPI

from grid_search.api.routes import router

app = FastAPI(
    title="Grid World Search API",
    version="0.1.0",
)

app.include_router(router)
