#main
import os
import signal
import time
import threading

from overlay_widget import KeystrokeOverlay
from keylogger import KeyListener
import gi

gi.require_version("Gtk", "4.0")
from gi.repository import Gtk

class KeystrokeApp(Gtk.Application):
    def __init__(self, device_path):
        super().__init__()
        self.device_path = device_path
        self.overlay = None
        self.listener = None

    def do_activate(self):
        self.overlay = KeystrokeOverlay()
        self.overlay.set_application(self)

        self.listener = KeyListener(self.device_path, self.overlay.update_keys)
        self.listener.start()

        self.overlay.present()


if __name__ == "__main__":
    DEVICE_PATH = "/dev/input/by-id/usb-2a7a_CASUE_USB_KB-event-kbd"
    app = KeystrokeApp(DEVICE_PATH)
    app.run([])


