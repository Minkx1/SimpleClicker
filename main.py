"""===== main.py ====="""

import time, threading
from pynput import keyboard
from pynput.mouse import Controller,Button

from settings import get_setting
from UI import ClickerUI

# Event to signal program stop
stop_event = threading.Event()

mouse = Controller()

def str_to_btn(str):
    if str=="left":
        return Button.left
    elif str=="right":
        return Button.right
    elif str=="middle":
        return Button.middle
    else:
        return Button.left

class Clicker():
    def __init__(self):
        self.hold = False
        self.released_hold = False
        self.pause = True  # pause state
        self.mode = get_setting("clicker_mode") # clicker mode
        self.button = str_to_btn(get_setting("mouse_button"))
        self.click_cooldown = 1 / int(get_setting('cps')) # time between clicks

    def on_press(self, key):
        try:
            start_stop_key = get_setting("hotkey_start").lower()
            quit_key = get_setting("hotkey_quit").lower()

            # Отримуємо назву натиснутої клавіші
            if hasattr(key, 'char') and key.char:
                pressed_key = key.char.lower()
            else:
                pressed_key = str(key).replace("Key.", "").lower()

            if pressed_key == start_stop_key:
                self.pause = not self.pause
                # print("⏸ Paused" if self.pause else "▶ Running")
                self.hold = False

            elif pressed_key == quit_key:
                self.pause = True
                stop_event.set()
                # print("❌ Exit")
                return False

        except Exception as e:
            print(f"Error in on_press: {e}")

    def run(self):
        # Main clicker loop
        while not stop_event.is_set():
            if not self.pause:  
                if self.mode == "single":
                    
                    mouse.click(self.button)
                    time.sleep(self.click_cooldown)

                elif self.mode == "double":

                    mouse.click(self.button, 2)
                    time.sleep(self.click_cooldown)

                elif self.mode == "hold":
                    if not self.hold:
                        mouse.press(self.button)
                        self.hold = True
            else:
                time.sleep(1.0)
        mouse.release(self.button) 

def start_ui():
    UI = ClickerUI()
    UI.run(stop_event=stop_event)

if __name__ == "__main__":
    # Start clicker
    clicker = Clicker()
    listener = keyboard.Listener(on_press=clicker.on_press)
    listener.start()

    clicker_thread = threading.Thread(target=clicker.run, daemon=True)
    clicker_thread.start()

    # Start GUI
    start_ui()