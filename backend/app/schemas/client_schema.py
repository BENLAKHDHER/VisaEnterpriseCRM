from pydantic import BaseModel


class ClientCreate(BaseModel):
    first_name: str
    last_name: str
    email: str
    phone: str
    passport_number: str

class ClientUpdate(BaseModel):
    first_name: str
    last_name: str
    email: str
    phone: str
    passport_number: str