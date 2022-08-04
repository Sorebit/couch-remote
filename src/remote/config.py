"""TODO:
   - Link to pynput Key documentation
   - Transform into pydantic Settings object
"""

from pynput.keyboard import Key

from remote.models import Button


BUTTONS = (
    Button(key=Key.media_play_pause, label='⏯️'),
    Button(key=Key.esc, label='Esc'),
    Button(key=Key.caps_lock, label='Caps Lock'),
    Button(key=Key.space, label='Space'),
)


# BUTTONS = {
#     'play_pause_media': Button(key=Key.media_play_pause, label='⏯️'),
#     'esc': Button(key=Key.esc, label='Esc'),
#     'caps': Button(key=Key.caps_lock, label='Caps Lock'),
#     'sp': Button(key=Key.space, label='Space'),
# }
