from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

import pyqrcode

app = FastAPI()
templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")

DEFAULT_URL = "https://arjon.es/"


@app.get("/", response_class=HTMLResponse)
async def root(request: Request):
    return templates.TemplateResponse("home.html", {"request": request, "url": DEFAULT_URL})


@app.post("/qr", response_class=HTMLResponse)
async def root(request: Request, url: str = Form(...)):
    code = pyqrcode.create(url)
    qr_data = code.png_as_base64_str(scale=5)
    return templates.TemplateResponse("home.html", {"request": request, "url": url, "qr_data": qr_data})
