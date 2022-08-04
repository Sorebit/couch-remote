from fastapi import FastAPI, Request

from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

import remote
from remote import config


app = FastAPI()
app.mount("/static", StaticFiles(packages=["remote"]), name="static")
templates = Jinja2Templates(directory="templates/")  # pewnie też zjebane

server = remote.Server(config)


@app.post('/p/{key}')
async def press_key(key: str):
    await server.press_once(key)
    return {"p": key}


@app.get('/')
async def index(request: Request):
    ctx = {
        'request': request,
        'buttons': server.get_buttons(),
    }
    return templates.TemplateResponse('index.html', context=ctx)


def main():
    print('Hello from main')
