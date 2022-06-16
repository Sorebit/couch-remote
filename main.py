from typing import Union

from fastapi import FastAPI
from pydantic import BaseModel
from pynput.keyboard import Key, Controller

import logging

app = FastAPI()


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

# class Key(BaseModel):
#     """Add validation with config???"""
#     key: str

class UnknownKeyError(Exception):
    pass


class Server:
    """W serverze robi się exposy, więc robi się na klasie dekorator"""
    # @expose(in_model=InModel, out_model=OutModel)
    # def method(self, request: InModel) -> OutModel:
    #     return OutModel()

    # def __init_subclass__(cls, **kwargs):
    #     wow
        # pass

    def __init__(self, config):
        self._config = config
        self._backend = PilotBackend()

    def press(self, key):
        self._validate_key(key)
        key = self._config.BUTTON_LIST[key]
        self._backend.press_key(key)
        logging.info(f'Pressed {key}')

    def release(self, key):
        self._validate_key(key)
        key = self._config.BUTTON_LIST[key]
        self._backend.release_key(key)
        logging.info(f'Released {key}')

    def _validate_key(self, key):
        if key not in self._config.BUTTON_LIST.keys():
            raise UnknownKeyError(key)

        return self._config.BUTTON_LIST[key]


import config
server = Server(config)


@app.get("/p/{k}")
def press_key(k: str):
    server.press(k)
    return {"p": k}


@app.get("/r/{k}")
def release_key(k: str):
    server.release(k)
    return {"r": k}
