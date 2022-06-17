import asyncio
import logging

from fastapi import FastAPI, Request
from pydantic import BaseModel
from pynput.keyboard import Key, Controller
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

import config

log = logging.getLogger()


app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates/")


class PilotBackend:
    """this is an abstract class, connected to the PC, so OS-dependent probably. just to be sure someone can add their
    backend easily."""

    def __init__(self):
        self.keyboard = Controller()
        # handle special keys easily
        # such as  media_play_pause

    def press_key(self, key: str):
        """Simulates keypress"""
        self.keyboard.press(key)

    def release_key(self, key: str):
        self.keyboard.release(key)


class UnknownKeyError(Exception):
    pass


class Server:
    """W serverze robi się exposy, więc robi się na klasie dekorator"""
    # @expose(in_model=InModel, out_model=OutModel)
    # def method(self, request: InModel) -> OutModel:
    #     return OutModel()

    def __init__(self, _config):
        self._config = _config
        self._backend = PilotBackend()

    async def press_once(self, key):
        self._validate_key(key)
        key = self._config.BUTTONS[key].key
        self._backend.press_key(key)
        await asyncio.sleep(0.1)
        self._backend.release_key(key)
        log.info(f'Pressed once: {key}')

    def _validate_key(self, key):
        if key not in self._config.BUTTONS.keys():
            raise UnknownKeyError(key)

        return self._config.BUTTONS[key]

    def get_buttons(self):
        return [
            {'label': btn.label, 'value': val}
            for val, btn in self._config.BUTTONS.items()
        ]


server = Server(config)

class KeyPress(BaseModel):
    key: str


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

