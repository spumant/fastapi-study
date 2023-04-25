from fastapi import Request


async def home(request: Request, id: str):
    return request.app.state.views.TemplateResponse("index.html", {"request": request, "id": id})
