from pydantic import BaseModel


class Client(BaseModel):
    firstName: str
    lastName: str
    phone: str
