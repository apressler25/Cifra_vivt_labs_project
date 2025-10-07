from fastapi import APIRouter, Depends
# from sqlalchemy.orm import Session
# from app.schemas.user import UserCreate
# from app.services.user_service import create_user
# from app.dependencies import get_db

router = APIRouter(prefix="/users", tags=["users"])


@router.get("/")
def read_root():
    return {"Hello": "World"}


# @router.post("/", response_model=UserCreate)
# def create_new_user(user: UserCreate, db: Session = Depends(get_db)):
#     return create_user(db, user)
