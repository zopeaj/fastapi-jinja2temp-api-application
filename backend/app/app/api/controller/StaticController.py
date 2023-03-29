from typing import Any
from fastapi import APIRouter, Request, Path
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

staticRouter = APIRouter()

staticRouter.mount("/static", StaticFiles(directory="static"))

templates = Jinja2Templates(directory="templates")

@staticRouter.get("/{data_id}", response_class=HTMLResponse)
async def read_data(request: Request, data_id: int = Path(...)):
    data = None
    if data_id in fake_db:
        data = fake_db[data_id]
    else:
        data = None
    return templates.TemplateResponse("data_details.htm", {"request": Request, "data": data})

@staticRouter.get("/", response_class=HTMLResponse)
async def read_datas(request: Request) -> Any:
    return templates.TemplateResponse("data_list.html", {"request": request, "data": fake_db})
