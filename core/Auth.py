from fastapi import Request
from fastapi.security import SecurityScopes


async def check_permissions(request: Request, security_scopes: SecurityScopes):
    """
    权限验证
    """
    pass
