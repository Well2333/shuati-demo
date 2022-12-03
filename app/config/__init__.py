from pydantic import BaseModel


class Server(BaseModel):
    host: str = "0.0.0.0"
    port: int = 8450


class User(BaseModel):
    disable_registration: bool = False
    """是否禁用用户注册"""
    disable_password_hash: bool = False
    """是否禁用密码哈希加密"""
    token_expired_time:int = 7200
    """用户token过期时间"""

class Config(BaseModel):
    server: Server
    user: User
