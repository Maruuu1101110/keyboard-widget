# config.py
import os, json

CONFIG_DIR = os.path.expanduser("~/.config/keyboard-widget")
CONFIG_PATH = os.path.join(CONFIG_DIR, "config.json")

def load_config():
    os.makedirs(CONFIG_DIR, exist_ok=True)
    if not os.path.exists(CONFIG_PATH):
        config = {}
    else:
        with open(CONFIG_PATH, 'r') as f:
            config = json.load(f)

    updated = False
    if "theme" not in config:
        config["theme"] = "default"
        updated = True
    if updated:
        save_config(config)

    return config

def save_config(config):
    os.makedirs(CONFIG_DIR, exist_ok=True)
    with open(CONFIG_PATH, 'w') as f:
        json.dump(config, f, indent=4)

