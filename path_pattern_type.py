# from fastapi import FastAPI

# app = FastAPI()


# @app.get("/")
# async def first():
#     return {"message": "Hello World"}


# # Async
# from fastapi import FastAPI
# import httpx


# app = FastAPI()


# @app.get("/")
# async def first():
#     async with httpx.AsyncClient() as client
#     results = await client.get('https://api.github.com/users/github')
#     return results

from fastapi import FastAPI

app = FastAPI()


@app.get("/items/{item_id}")
async def read_item(item_id: float):
    return {"item_id": item_id}

@app.get("/items1/{item_id}")
async def read_item_float(item_id: float):
    return {"item_id": item_id}


@app.get("/items2/{item_id}")
async def read_item_bool(item_id: bool):
    return {"item_id": item_id}