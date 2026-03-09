# Async
from fastapi import FastAPI
import httpx


app = FastAPI()


@app.get("/")
async def first():
    async with httpx.AsyncClient() as client
    results = await client.get('https://api.github.com/users/github')
    return results
