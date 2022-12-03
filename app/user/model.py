from typing import Literal

from pydantic import BaseModel, validator

from ..utils.tools import sql_checker


class History(BaseModel):
    user_name: str
    lib: str
    question: str
    type: Literal[0, 1, 2]
    note: str | None = "NULL"

    _user_name = validator("user_name", pre=True, allow_reuse=True)(
        sql_checker
    )
    _lib = validator("lib", pre=True, allow_reuse=True)(sql_checker)
    _question = validator("question", pre=True, allow_reuse=True)(sql_checker)
    _note = validator("note", pre=True, allow_reuse=True)(sql_checker)


class Favorate(BaseModel):
    user_name: str
    lib: str
    question: str
    folder: str

    _user_name = validator("user_name", pre=True, allow_reuse=True)(
        sql_checker
    )
    _lib = validator("lib", pre=True, allow_reuse=True)(sql_checker)
    _question = validator("question", pre=True, allow_reuse=True)(sql_checker)
    _folder = validator("folder", pre=True, allow_reuse=True)(sql_checker)
