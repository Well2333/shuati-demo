from pathlib import Path

from aiosqlite import Connection, connect

from .model import History, Favorate

from ..utils.tools import get_utc_time, sql_checker


class User:
    uid: int
    tokens: dict[str, str]
    home: Path
    _db: Connection

    def __init__(self, uid, token, db):
        self.uid = uid
        self.home = Path(f"data/users/{uid}")
        self.tokens[token] = get_utc_time()
        self._db = db

    @staticmethod
    def is_exists(uid: int):
        '''判断用户的本地文件是否存在'''
        return {
            "home": bool(Path(f"data/users/{uid}").exists()),
            "database": bool(
                Path(f"data/users/{uid}/datebase.sqlite").exists()
            ),
            "config": bool(Path(f"data/users/{uid}/config.json").exists()),
        }

    @staticmethod
    async def create_user(uid: int):
        '''创建用户的本地文件，初始化数据库'''
        home = Path(f"data/users/{uid}")
        home.mkdir(755, True, True)
        async with connect(home.joinpath("datebase.sqlite")) as db:
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
            await db.commit()

    @staticmethod
    def get(uid: int, token: str):
        '''获取用户实例，若不存在则返回None'''
        global users
        if uid in users.keys() and token in users[uid].tokens.keys():
            users[uid].tokens = get_utc_time()
            return users[uid]
        return None

    @classmethod
    async def login(cls, uid: int, token: str):
        '''获取用户实例，若实例不存在则创建新的实例并返回，若用户本身不存在则返回None'''
        global users
        if uid in users.keys():
            if token not in users[uid].tokens:
                users[uid].tokens[token] = get_utc_time()
        elif cls.is_exists(uid):
            users[uid] = cls(
                uid=uid,
                token=token,
                db=await connect(Path(f"data/users/{uid}/datebase.sqlite")),
            )
        else:
            return None
        return users[uid]

    async def logout(self, token: str):
        '''用户实例登出，若登出成功则返回True，若token不存在则返回False'''
        global users
        if token not in self.tokens:
            return False
        self.tokens.pop(token)
        if len(self.tokens):
            await self._db.commit()
            await self._db.close()
            users.pop[self.uid]
        return True
    
    def _check_update_token(self,token):
        '''检查token是否存在，若存在则更新token的时间'''
        if token not in self.tokens.keys():
            raise KeyError(f"user {self.uid} do not have {token}")
        ct = get_utc_time()
        self.tokens[token] = ct
        return ct

    async def log_history(self, history: History, token: str):
        '''记录做题记录'''
        ct = self._check_update_token(token)
        await self._db.execute(
            f"INSERT INTO history (time,lib,question,type,note) VALUES \
            ({ct}, '{history.lib}', '{history.question}', '{history.type}', '{history.note}' )"
        )
        await self._db.commit()

    async def load_history_libs(self, token:str):
        '''读取已读的题库'''
        self._check_update_token(token)
        cursor = await self._db.execute("SELECT lib FROM history")
        return {row[0] async for row in cursor}

    async def load_history_questions(self, lib, token:str):
        '''读取此题库中全部做题记录'''
        self._check_update_token(token)
        cursor = await self._db.execute(
            f"SELECT question,type FROM history WHERE lib = '{sql_checker(lib)}'"
        )
        return {{row[0]: row[1]} async for row in cursor}

    async def add_favorate(self, favorate: Favorate, token:str):
        '''添加收藏'''
        ct = self._check_update_token(token)
        await self._db.execute(
            f"INSERT INTO favorate (time,lib,question,folder) VALUES \
            ({ct}, '{favorate.lib}', '{favorate.question}', '{favorate.folder}')"
        )
        await self._db.commit()

    async def remove_favorate(self, favorate: Favorate, token:str):
        '''移除收藏'''
        self._check_update_token(token)
        await self._db.execute(
            f"DELETE FROM favorate WHERE lib = '{favorate.lib}' AND question = '{favorate.question}' AND folder = '{favorate.folder}'"
        )
        await self._db.commit()

    async def load_favorate_folders(self, token:str):
        '''读取收藏夹'''
        self._check_update_token(token)
        cursor = await self._db.execute("SELECT folder FROM favorate")
        return {row[0] async for row in cursor}

    async def load_favorate_questions(self, folder, token:str):
        '''读取此收藏夹中的全部问题'''
        self._check_update_token(token)
        cursor = await self._db.execute(
            f"SELECT lib,question FROM favorate WHERE folder = '{sql_checker(folder)}'"
        )
        return {{"lib": row[0], "question": row[1]} async for row in cursor}


users: dict[int, User] = {}
