# keylogger.py
from evdev import InputDevice, categorize, ecodes
from threading import Thread
from gi.repository import GLib

class KeyListener:
    def __init__(self, device_path, on_update):
        self.dev = InputDevice(device_path)
        self.keys_pressed = set()
        self.on_update = on_update

    def start(self):
        def loop():
            for event in self.dev.read_loop():
                if event.type == ecodes.EV_KEY:
                    key_event = categorize(event)
                    key_name = key_event.keycode if isinstance(key_event.keycode, str) else key_event.keycode[0]
                    if key_event.keystate == key_event.key_down:
                        self.keys_pressed.add(key_name)
                    elif key_event.keystate == key_event.key_up:
                        self.keys_pressed.discard(key_name)

                    GLib.idle_add(self.on_update, [self.map_key(k) for k in self.keys_pressed])

        Thread(target=loop, daemon=True).start()

    def map_key(self, raw_code):
        key = raw_code.replace("KEY_", "").upper()
        return {
            "CAPSLOCK": "CAPS",
            "ENTER": "ENTER",
            "BACKSPACE": "BACKSPACE",
            "LEFTSHIFT": "SHIFT-L",
            "RIGHTSHIFT": "SHIFT-R",
            "LEFTCTRL": "CTRL-L",
            "RIGHTCTRL": "CTRL-R",
            "LEFTALT": "ALT-L",
            "RIGHTALT": "ALT-R",
            "LEFTMETA": "SUPER",
            "RIGHTMETA": "SUPER",
            "ESC": "ESC",
            "SPACE": "SPACE",
            "TAB": "TAB",
            "MENU": "MENU",
            "RIGHT": ">",
            "LEFT": "<",
            "UP": "^",
            "COMMA": ",",
            "DOT": ".",
            "SLASH": "/",
            "SEMICOLON": ";",
            "APOSTROPHE": "'",
            "BACKSLASH": '\\',
            "LEFTBRACE": "[",
            "RIGHTBRACE": "]",
            "MINUS": "-",
            "EQUAL": "=",
            "GRAVE": "`"
        }.get(key, key)



        

