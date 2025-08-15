"""===== settings.py ====="""

import os, json

version = '0.1.0'  # program version

# Paths for settings folder and file
SETTINGS_DIR = os.path.join(os.getenv("APPDATA"), "SimpleClicker")
SETTINGS_FILE = os.path.join(SETTINGS_DIR, "settings.json")

os.makedirs(SETTINGS_DIR, exist_ok=True)

# Default settings
DEFAULT_SETTINGS = {
    "cps": 10,
    "mouse_button": "left",
    "hotkey_start": "F6",
    "hotkey_stop": "F7"
}

# Current settings (loaded from file or defaults)
SETTINGS = DEFAULT_SETTINGS.copy()

def load_settings():
    """Load settings from JSON file"""
    if os.path.exists(SETTINGS_FILE):
        try:
            with open(SETTINGS_FILE, "r", encoding="utf-8") as f:
                loaded = json.load(f)
                SETTINGS.update(loaded)
        except Exception as e:
            print(f"[ERROR] Failed to load settings: {e}")
    else:
        # Create default settings file if it doesn't exist
        with open(SETTINGS_FILE, "w", encoding="utf-8") as f:
            json.dump(DEFAULT_SETTINGS, f, ensure_ascii=False, indent=4)

def save_settings():
    """Save current settings to JSON file"""
    try:
        with open(SETTINGS_FILE, "w", encoding="utf-8") as f:
            json.dump(SETTINGS, f, ensure_ascii=False, indent=4)
    except Exception as e:
        print(f"[ERROR] Failed to save settings: {e}")

def get_setting(key):
    """Get a setting value by key"""
    return SETTINGS.get(key, DEFAULT_SETTINGS.get(key))

def set_setting(key, value):
    """Set a setting value and save to file"""
    SETTINGS[key] = value
    save_settings()

# Load settings on module import
load_settings()
