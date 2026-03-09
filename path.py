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

# from fastapi import FastAPI

# app = FastAPI()


# @app.get("/users/me")
# async def read_users_me():
#     return {"Users: the current user" }


# @app.get("/users/{user_id}")
# async def read_users(user_id: int):
#     return {"Users: ": user_id}



from fastapi import FastAPI

app = FastAPI()


@app.get("/users")
async def read_user():
    return ("bappy","Akram")


@app.get("/users")
async def get_user():
    return {"Hi","I", "am","Bappy"}