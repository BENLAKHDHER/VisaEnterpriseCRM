from fastapi import APIRouter
from fastapi import Depends

from sqlalchemy.orm import Session

from app.database.connection import get_db

from app.schemas.client_schema import ClientCreate

from app.repositories.client_repository import create_client

from app.repositories.client_repository import get_clients

from app.repositories.client_repository import get_client_by_id

from app.schemas.client_schema import ClientUpdate

from app.repositories.client_repository import update_client

from app.repositories.client_repository import delete_client

from app.core.auth_dependency import (
    get_current_user
)


router = APIRouter()


@router.post("/clients")
def create_new_client(
    client: ClientCreate,
    db: Session = Depends(get_db)
):
    return create_client(db, client)

@router.get("/clients")
def read_clients(
    current_user=Depends(
        get_current_user
    ),
    db: Session = Depends(get_db)
):
    return get_clients(db)

@router.get("/clients/{client_id}")
def read_client(
    client_id: int,
    db: Session = Depends(get_db)
):
    return get_client_by_id(
        db=db,
        client_id=client_id
    )

@router.put("/clients/{client_id}")
def update_existing_client(
    client_id: int,
    client: ClientUpdate,
    db: Session = Depends(get_db)
):
    return update_client(
        db=db,
        client_id=client_id,
        client_data=client
    )

@router.delete("/clients/{client_id}")
def remove_client(
    client_id: int,
    db: Session = Depends(get_db)
):
    return delete_client(
        db=db,
        client_id=client_id
    )