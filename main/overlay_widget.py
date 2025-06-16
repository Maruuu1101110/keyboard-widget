# overlay_widget.py
import os
import gi
gi.require_version("Gtk", "4.0")
from gi.repository import Gtk, Gdk, GLib

CONFIG_DIR = os.path.join(os.path.expanduser("~"), ".config", "keyboard-widget")
STYLE_PATH = os.path.join(CONFIG_DIR, "themes","default.css")
CONFIG_PATH = os.path.join(CONFIG_DIR, "config.json")

os.makedirs(CONFIG_DIR, exist_ok=True)


class KeystrokeOverlay(Gtk.Window):
    def __init__(self):
        super().__init__()
        self.set_decorated(False)
        self.set_title("Keystroke Overlay")
        self.set_resizable(True)
        self.set_opacity(1)
        self.set_can_focus(False)

        self.key_buttons = {}
        self.set_css()

        self.vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=8)
        self.vbox.set_margin_top(12)
        self.vbox.set_margin_bottom(12)
        self.vbox.set_margin_start(24)
        self.vbox.set_margin_end(24)

        self.create_rows()
        self.set_child(self.vbox)

    def create_rows(self):
        keyboard_rows = [
            (8, ["`", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "-", "=", "BACKSPACE"]),
            (8, ["TAB", "Q", "W", "E", "R", "T", "Y", "U", "I", "O", "P", "[", "]", "\\"]),
            (8, ["CAPS", "A", "S", "D", "F", "G", "H", "J", "K", "L", ";", "'", "ENTER"]),
            (8, ["SHIFT-L", "Z", "X", "C", "V", "B", "N", "M", ",", ".", "/", "SHIFT-R"]),
            (36, ["CTRL-L", "SUPER", "ALT-L", "SPACE", "ALT-R", "CTRL-R"]),
        ]

        for margin_start, keys in keyboard_rows:
            row = Gtk.Box(spacing=10)
            row.set_margin_start(0)
            row.set_halign(Gtk.Align.CENTER)
            for key in keys:
                btn = self.make_button(key)
                row.append(btn)
            self.vbox.append(row)

    def make_button(self, key):
        btn = Gtk.Button(label=key.lower())
        btn.set_sensitive(False)
        btn.set_can_focus(False)
        btn.set_focus_on_click(False)
        btn.add_css_class("unpressed")
        btn.set_valign(Gtk.Align.CENTER)

        wide_keys = {
            "TAB": 60, "CAPS": 70, "SHIFT": 90, "ENTER": 80, "BACKSPACE": 80,
            "CTRL": 50, "META": 50, "ALT": 50, "MENU": 50, "SPACE": 300
        }
        width = wide_keys.get(key.upper(), 45)
        btn.set_size_request(width, 45)
        self.key_buttons[key.upper()] = btn
        return btn

    def set_css(self, theme_path=None):
        provider = Gtk.CssProvider()
        if theme_path and os.path.exists(theme_path):
            with open(theme_path, "rb") as f:
                provider.load_from_data(f.read())
        else:
            provider.load_from_data(b""" 
                window {
                    background-color: rgba(30,30,46, 0.0);
                }

                button {
                    color: #7493D4;
                    background: rgba(30,30,56, 0.85);
                    border-radius: 6px;
                    padding: 10px;
                    border: 1px solid #7493D4;
                    transition: 100ms ease-in-out;
                }

                button label {
                    color: #7493D4;
                    font-family: monospace;
                    font-size: 16px;
                }

                .pressed {
                    background: #647fba;
                    font-weight: bold;
                }

                .unpressed {
                    background: rgba(30,30,56, 0.85);
                }

             """)

        Gtk.StyleContext.add_provider_for_display(
            Gdk.Display.get_default(), provider,
            Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION
        )
        print("No custom theme found. You can create one at ~/.config/keyboard-widget/default.css")


    def update_keys(self, keys):
        special_chars = {
            '`': '~', '1': '!', '2': '@', '3': '#', '4': '$',
            '5': '%', '6': '^', '7': '&', '8': '*', '9': '(',
            '0': ')', '-': '_', '=': '+', '[': '{', ']': '}',
            ';': ':', "'": '"', '\\': '|', ',': '<', '.': '>', '/': '?'
        }
        shift_pressed = 'SHIFT-L' in keys or 'SHIFT-R' in keys
        for key, btn in self.key_buttons.items():
            label = key
            if shift_pressed and key in special_chars:
                label = special_chars[key]
            elif shift_pressed and len(key) == 1:
                label = key.upper()
            else:
                label = key.lower()
            btn.set_label(label)

            if key in keys:
                btn.remove_css_class("unpressed")
                btn.add_css_class("pressed")
            else:
                btn.remove_css_class("pressed")
                btn.add_css_class("unpressed")


            
