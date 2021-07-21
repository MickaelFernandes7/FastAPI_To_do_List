from fastapi import FastAPI
from a_fazer import router as a_fazer_router

app = FastAPI()

app.include_router(a_fazer_router, prefix="/a-fazer", tags=["To Do"])