from enum import Enum

from pydantic import BaseModel, ConfigDict
from typing import Union


class User(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    username: str
    email: Union[str, None] = None
    first_name: Union[str, None] = None
    last_name: Union[str, None] = None
    active: Union[bool, None] = True
    is_admin: Union[bool, None] = False


class UserCreating(User):
    password: str


class UserFull(User):

    id: Union[int, None] = None


class UserInDB(User):
    hashed_password: str


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: Union[str, None] = None


class Roles(str, Enum):
    admin = 'admin'
    user = 'user'
    guest = 'guest'
