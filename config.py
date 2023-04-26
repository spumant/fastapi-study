import os.path
from pydantic import BaseSettings
from typing import List
from dotenv import load_dotenv, find_dotenv


class Config(BaseSettings):
    # 加载环境变量
    load_dotenv(find_dotenv(), override=True)
    # 调试模式
    APP_DEBUG: bool = True
    # 项目信息
    VERSION: str = "0.0.1"
    PROJECT_NAME: str = "fastapi-demo"
    DESCRIPTION: str = 'fastapi项目demo'
    # 静态资源目录
    STATIC_DIR: str = os.path.join(os.getcwd(), "static")
    # 跨域请求
    CORS_ORIGINS: List[str] = ['*']
    CORS_ALLOW_CREDENTIALS: bool = True
    CORS_ALLOW_METHODS: List[str] = ['*']
    CORS_ALLOW_HEADERS: List[str] = ['*']
    TEMPLATE_DIR: str = "static/template"


settings = Config()
