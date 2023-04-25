from typing import List
from pydantic import BaseModel


class Login(BaseModel):
    username: str
    password: str


async def index():
    return {"fun": "/login"}


async def login(data: Login):
    return data
