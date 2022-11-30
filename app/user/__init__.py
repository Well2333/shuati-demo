from pathlib import Path

from aiosqlite import Connection, connect

from .model import History, Favorate

from ..utils.timetools import get_utc_time


class User:
    home: Path
    db: Connection

    @classmethod
    async def init(cls, user_name: str):
        user = cls()
        home = Path(f"data/users/{user_name}")
        user.home = home
        if home.joinpath("datebase.sqlite").exists():
            db = await connect(f"{home}/datebase.sqlite")
        else:
            home.mkdir(755, True, True)
            db = await connect(f"{home}/datebase.sqlite")
            await db.execute(
                'CREATE TABLE history (\
                    id       INT PRIMARY KEY NOT NULL,\
                    time     DATETIME        NOT NULL, \
                    lib      TEXT            NOT NULL,\
                    question TEXT            NOT NULL,\
                    type     INTEGER         NOT NULL,\
                    note     TEXT);'
            )
            await db.execute(
                'CREATE TABLE favorate (\
                    id       INT PRIMARY KEY NOT NULL,\
                    time     DATETIME        NOT NULL, \
                    lib      TEXT            NOT NULL,\
                    question TEXT            NOT NULL,\
                    folder   TEXT            NOT NULL DEFAULT "default");'
            )
        user.db = db
        return user

    @staticmethod
    def is_exists(user_name: str):
        return bool(Path(f"data/users/{user_name}").exists())

    async def log_history(self, history: History):
        await self.db.execute(
            f"INSERT INTO history (time,lib,question,type,note) VALUES \
            ({get_utc_time()}, '{history.lib}', '{history.question}', '{history.type}', '{history.note}' )"
        )

    async def load_history_libs(self):
        cursor = await self.db.execute("SELECT lib FROM history")
        return {row[0] for row in cursor}

    async def load_history_questions(self, lib):
        cursor = await self.db.execute(
            f"SELECT question,type FROM history WHERE lib = '{lib}'"
        )
        return {{row[0]: row[1]} for row in cursor}

    async def add_favorate(self, favorate: Favorate):
        await self.db.execute(
            f"INSERT INTO favorate (time,lib,question,folder) VALUES \
            ({get_utc_time()}, '{favorate.lib}', '{favorate.question}', '{favorate.folder}')"
        )

    async def remove_favorate(self, favorate: Favorate):
        await self.db.execute(
            f"DELETE FROM favorate WHERE lib = '{favorate.lib}' AND question = '{favorate.question}' AND folder = '{favorate.folder}'"
        )

    async def load_favorate_folders(self):
        cursor = await self.db.execute("SELECT folder FROM favorate")
        return {row[0] for row in cursor}

    async def load_favorate_questions(self, folder):
        cursor = await self.db.execute(
            f"SELECT lib,question FROM favorate WHERE folder = '{folder}'"
        )
        return {{"lib": row[0], "question": row[1]} for row in cursor}
