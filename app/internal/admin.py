from fastapi import APIRouter

router = APIRouter(prefix="/admin", tags=["admin"])

@router.get("/")
def get_admin_dashboard():
    return {"message": "login"}

@router.get("/dashboard")
def get_admin_dashboard():
    return {"message": "Admin Dashboard"}