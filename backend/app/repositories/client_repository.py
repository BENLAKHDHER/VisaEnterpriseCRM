from sqlalchemy.orm import Session

from app.models.client import Client
from app.schemas.client_schema import ClientCreate
from app.schemas.client_schema import ClientUpdate


def create_client(
    db: Session,
    client_data: ClientCreate
):
    client = Client(
        first_name=client_data.first_name,
        last_name=client_data.last_name,
        email=client_data.email,
        phone=client_data.phone,
        passport_number=client_data.passport_number
    )

    db.add(client)

    db.commit()

    db.refresh(client)

    return client

def get_clients(db: Session):
    return db.query(Client).all()

def get_client_by_id(
    db: Session,
    client_id: int
):
    return (
        db.query(Client)
        .filter(Client.id == client_id)
        .first()
    )

def update_client(
    db: Session,
    client_id: int,
    client_data: ClientUpdate
):
    client = (
        db.query(Client)
        .filter(Client.id == client_id)
        .first()
    )

    if not client:
        return None

    client.first_name = client_data.first_name
    client.last_name = client_data.last_name
    client.email = client_data.email
    client.phone = client_data.phone
    client.passport_number = client_data.passport_number

    db.commit()

    db.refresh(client)

    return client

def delete_client(
    db: Session,
    client_id: int
):
    client = (
        db.query(Client)
        .filter(Client.id == client_id)
        .first()
    )

    if not client:
        return None

    db.delete(client)

    db.commit()

    return {
        "message": "Client supprimé avec succès"
    }
