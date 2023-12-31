from typing import Optional
from pydantic import BaseModel


class User(BaseModel):
    name: str
    email: str
    password: str
    class Config():
        orm_mode = True


class ShowAllUser(BaseModel):
     id: int
     name: str
     email: str

     class Config():
        orm_mode = True


class ShowUser(BaseModel):
    name: str
    email: str

    class Config():
        orm_mode = True


class Login(BaseModel):
    username: str
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    email: Optional[str] = None
