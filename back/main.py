from contextlib import asynccontextmanager

import uvicorn
from fastapi import FastAPI


@asynccontextmanager
async def lifespan(app: FastAPI):
    yield


app = FastAPI(
    title="chat",
    docs_url="/api/docs",
    redoc_url="/api/redoc",
    lifespan=lifespan,
)

# app.include_router(login_router)


@app.get("/api/check")
async def check():
    return {"chat_api": "ok"}


@app.get("/api/ask_chat/{question}")
async def ask_chat(question: str):
    return {"chat_api": "ok"}


if __name__ == "__main__":
    uvicorn.run(
        app,
        host="localhost",
        port=8000,
    )
