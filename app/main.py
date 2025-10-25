
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

app.include_router(userrouter)
app.include_router(homerouter)
app.include_router(my_programs_router)
app.include_router(statistics_router)
app.include_router(hystory_workout_router)
app.include_router(session_workout_router)
