#main
import os
import gi
gi.require_version("Gtk", "4.0")
from gi.repository import Gtk

from overlay_widget import KeystrokeOverlay
from keylogger import KeyListener
from config import load_config, save_config

class KeystrokeApp(Gtk.Application):
    def __init__(self, device_path, theme):
        super().__init__()
        self.device_path = device_path
        self.theme = theme
        self.overlay = None
        self.listener = None

    def do_activate(self):
        self.overlay = KeystrokeOverlay()

        #Theme loading
        theme_path = os.path.expanduser(
            f"~/.config/keyboard-widget/themes/{self.theme}.css"
        )
        self.overlay.set_css(theme_path)

        self.overlay.set_application(self)
        self.listener = KeyListener(self.device_path, self.overlay.update_keys)
        self.listener.start()
        self.overlay.present()

def choose_keyboard_device():
    by_id_dir = "/dev/input/by-id"
    if not os.path.exists(by_id_dir):
        print("❌ /dev/input/by-id/ not found! Are you on Linux?")
        return None

    devices = []
    print("\n== Available keyboard-like devices ==")
    for entry in sorted(os.listdir(by_id_dir)):
        if "kbd" in entry.lower():
            full_path = os.path.join(by_id_dir, entry)
            if os.path.islink(full_path):
                devices.append(full_path)

    if not devices:
        print("❌ No keyboard-like devices found in /dev/input/by-id/")
        return None

    for idx, dev in enumerate(devices, 1):
        print(f"[{idx}] {os.path.basename(dev)} → {os.path.realpath(dev)}")

    while True:
        try:
            choice = int(input("Pick a device by number: "))
            if 1 <= choice <= len(devices):
                return devices[choice - 1]
            else:
                print("❌ Invalid choice. Try again.")
        except ValueError:
            print("⚠️ Please enter a number.")

if __name__ == "__main__":
    config = load_config()
    device_path = config["device_path"]
    theme = config["theme"]

    print(f"✅ Using device: {device_path}")
    print(f"🎨 Using theme: {theme}")
    app = KeystrokeApp(device_path, theme)
    app.run([])
