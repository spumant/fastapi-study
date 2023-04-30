import hashlib
import uuid
from passlib.handlers.pbkdf2 import pbkdf2_sha256


def random_str():
    """
    唯一随机字符串
    """
    only = hashlib.md5(str(uuid.uuid1()).encode(encoding='UTF-8')).hexdigest()
    return str(only)


def en_password(pwd: str):
    """
    密码加密
    """
    password = pbkdf2_sha256.hash(pwd)
    return password


def check_password(password: str, old: str):
    """
    密码校验
    """
    check = pbkdf2_sha256.verify(password, old)
    if check:
        return True
    else:
        return False
