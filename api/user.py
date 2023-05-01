"""
用户管理
"""
from core.Response import fail, success
from validator.user import CreateUser, AccountLogin, UserInfo
from models.base import User
from core.Utils import en_password, check_password
from core.Auth import create_access_token
from fastapi import Request
from fastapi.responses import JSONResponse


async def user_info(request: Request):
    """
    获取当前登录用户的信息
    """
    user_data = await User.get_or_none(pk=request.state.user_id)
    if not user_data:
        return fail(msg=f"用户ID{request.state.user_id}不存在！")
    return success(msg="用户信息", data=UserInfo(**user_data.__dict__))


async def user_add(post: CreateUser):
    """
    创建用户
    """
    post.password = en_password(post.password)
    create_user = await User.create(**post.dict())
    if not create_user:
        return fail(msg=f"用户{post.username}创建失败!")
    return success(msg=f"用户{create_user.username}创建成功")


async def user_del(user_id: int):
    """
    删除用户
    """
    delete_user = await User.filter(pk=user_id).delete()
    if not delete_user:
        return fail(msg=f"用户{user_id}删除失败!")
    return success(msg="删除成功")


async def account_login(post: AccountLogin):
    get_user = await User.get_or_none(username=post.username)
    if not get_user:
        return fail(msg=f"用户{post.username}密码验证失败！")
    if not check_password(post.password, get_user.password):
        return fail(msg=f"用户{post.username}密码验证失败！")
    if not get_user.user_status:
        return fail(msg=f"用户{post.username}已被管理员禁用！")
    jwt_data = {
        "user_id": get_user.pk,
        "user_type": get_user.user_type
    }
    jwt_token = create_access_token(data=jwt_data)
    # return success(msg="登陆成功😄", data={"token": jwt_token})
    return JSONResponse({
        "code": 200,
        "message": "登陆成功😄",
        "data": {
            "token": jwt_token
        }
    }, status_code=200, headers={"Set-Cookie": "X-token=Bearer " + jwt_token})
