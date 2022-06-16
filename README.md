# Pilot

A simple **remote control** for your PC keyboard.

> Currently, a proof of concept:
> - `POST /p/<key>` Presses key on host machine
> - `POST /r/<key>` Releases key on host machine
> - Tested only on Windows
> - Run with `uvicorn main:app --host 0.0.0.0 --port 8000`

---

- Easy install using `pip`.
- Specify the keys, you would like to be able to press in `config.py` using pynput.
- Serve the remote locally and use it on your phone or whatever. 

## Usage
In a venv do:
- `pip install pilot` - to install
- `pilot config` - to create a sample configuration file
- `pilot serve --local` - to serve over local network
- Access at url provided that gets printed out 

## Config

```python
from pynput.keyboard import Key

BUTTON_LIST = {
    'play_pause_media': Key.media_play_pause,
    'esc': Key.esc,
    'sp': Key.space,
}
```
