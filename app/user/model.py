from typing import Literal

from pydantic import BaseModel


class History(BaseModel):
    user_name: str
    lib: str
    question: str
    type: Literal[0, 1, 2]
    note: str | None = "NULL"


class Favorate(BaseModel):
    user_name: str
    lib: str
    question: str
    folder: str
