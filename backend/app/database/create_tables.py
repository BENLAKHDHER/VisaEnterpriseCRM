from app.database.base import Base
from app.database.connection import engine

from app.models.client import Client

from app.models.user import User


def create_tables():
    Base.metadata.create_all(bind=engine)


if __name__ == "__main__":
    create_tables()

    print("Tables créées avec succès")