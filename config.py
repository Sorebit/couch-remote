"""TODO: Link to pynput Key documentation"""

from pynput.keyboard import Key

from models import Button


BUTTONS = {
    'play_pause_media': Button(key=Key.media_play_pause, label='⏯️'),
    'esc': Button(key=Key.esc, label='Esc'),
    'caps': Button(key=Key.caps_lock, label='Caps Lock'),
    'sp': Button(key=Key.space, label='Space'),
}
