from sqlalchemy.orm import Session

from app.models.user import User

from app.schemas.user_schema import UserCreate

from app.core.security import hash_password

from app.core.security import verify_password


def create_user(
    db: Session,
    user_data: UserCreate
):
    user = User(
        username=user_data.username,
        email=user_data.email,
        password_hash=hash_password(
            user_data.password
        )
    )

    db.add(user)

    db.commit()

    db.refresh(user)

    return user

def get_user_by_username(
    db: Session,
    username: str
):
    return (
        db.query(User)
        .filter(User.username == username)
        .first()
    )

def authenticate_user(
    db: Session,
    username: str,
    password: str
):
    user = get_user_by_username(
        db=db,
        username=username
    )

    if not user:
        return None

    if not verify_password(
        password,
        user.password_hash
    ):
        return None

    return user

def get_user_from_token(
    db: Session,
    username: str
):
    return (
        db.query(User)
        .filter(User.username == username)
        .first()
    )