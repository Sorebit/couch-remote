# Couch Remote

A utility, available at [pypi](#). Download it on a computer and serve yourself a remote keyboard to control it.

## Usage
1. **To install:** `pip install couch-remote` (in a venv or globally with `-g`)
2. Now, your `remote` is available.
3. **Optionally,** `remote scaffold-config`, creates a basic settings file, then `remote global settings.py` copies it to a [global configuration directory](#install-a-global-settings-file-pilot-global-settingspy).
4.  **Finally,** `remote control` serves an instance at [localhost:4444](http://localhost:4444). This is the **only** command, you're going to need from now on.

## Settings

And how to set them.

```python
from pynput.keyboard import Key

BUTTON_LIST = {
    'play_pause_media': Key.media_play_pause,
    'esc': Key.esc,
    'sp': Key.space,
}
```

Q: Do jakiego formatu zapisują się i wczytują configi w settingsach?

How do you host an async app?1

### Install a global settings file `remote global settings.py `

When ran, stores settings at a default path: `~/.config/pilot/settings.py`

Pilot will default to this path when not specified.

Wchodzisz sobie na telefonie na tym samym wifi i pokazują ci się przyciski. Jak klikniesz ten przycisk, to po ws się wysyła nazwa przycisku, a serwer klika systemowo spację.