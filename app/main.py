from fastapi import FastAPI
from app.api.v1.reason import router as reason_router

app = FastAPI()

app.include_router(reason_router)
