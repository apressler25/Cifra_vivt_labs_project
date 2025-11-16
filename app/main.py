
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers.users import userrouter
from routers.home_page import homerouter 
from routers.my_programs import my_programs_router
from routers.statistics import statistics_router
from routers.hystory_workout import hystory_workout_router
from routers.session_workout import session_workout_router 
app = FastAPI(title="My App")

# Настройка CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # В продакшене укажите конкретные домены
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


routers = [userrouter, homerouter, my_programs_router, statistics_router, hystory_workout_router, session_workout_router]

for router in routers:
    app.include_router(router, prefix="/api")
