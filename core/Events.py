from typing import Callable
from fastapi import FastAPI
from database.mysql import register_mysql


def startup(app: FastAPI) -> Callable:
    """
    FastApi 启动完成事件
    :param app: FastAPI
    :return: start_app
    """

    async def app_start() -> None:
        # 注册数据库
        await register_mysql(app)
        # APP启动完成后触发
        print("启动完毕")
        pass

    return app_start


def stopping(app: FastAPI) -> Callable:
    """
    FastApi 停止事件
    :param app: FastAPI
    :return: stop_app
    """

    async def stop_app() -> None:
        # APP停止时触发
        print("停止")
        pass

    return stop_app
