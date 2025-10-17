
from fastapi import FastAPI
from routers.users import userrouter
app = FastAPI(title="My App")
app.include_router(userrouter)


