from pydantic import BaseModel
from pynput.keyboard import Key


class Button(BaseModel):
    key: Key
    label: str
