from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException

from sqlalchemy.orm import Session

from app.database.connection import get_db

from app.schemas.user_schema import UserLogin

from app.repositories.user_repository import (
    authenticate_user
)

from app.core.security import (
    create_access_token
)

from app.core.auth_dependency import get_current_user

router = APIRouter()


@router.post("/auth/login")
def login(
    credentials: UserLogin,
    db: Session = Depends(get_db)
):
    user = authenticate_user(
        db,
        credentials.username,
        credentials.password
    )

    if not user:
        raise HTTPException(
            status_code=401,
            detail="Invalid credentials"
        )

    token = create_access_token(
        {
            "sub": user.username
        }
    )

    return {
        "access_token": token,
        "token_type": "bearer"
    }


@router.get("/auth")
def auth_status():
    return {
        "status": "Auth module ready"
    }

@router.get("/me")
def get_me(
    current_user=Depends(get_current_user)
):
    return current_user