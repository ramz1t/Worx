from pydantic import BaseModel


class ApiNewAuth(BaseModel):
    email: str
    password: str
