from fastapi import APIRouter
from fastapi import Depends

from sqlalchemy.orm import Session

from app.database.connection import get_db

from app.schemas.user_schema import UserCreate

from app.repositories.user_repository import create_user


router = APIRouter()


@router.post("/users")
def create_new_user(
    user: UserCreate,
    db: Session = Depends(get_db)
):
    return create_user(db, user)