from fastapi import FastAPI
from routers import users, base
from internal import admin

app = FastAPI()

app.include_router(users.router)
app.include_router(admin.router)
# app.include_router(base.router)


@app.get("/")
def read_root():
    return {"Hello": "World"}
