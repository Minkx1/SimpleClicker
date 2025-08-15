"""===== main.py ====="""

import pyautogui, time, threading
from pynput import keyboard
from settings import get_setting
from UI import ClickerUI

# Event to signal program stop
stop_event = threading.Event()

class Clicker():
    def __init__(self):
        self.click_cooldown = 1 / int(get_setting('cps'))  # time between clicks
        self.button = get_setting('mouse_button')
        self.pause = True  # pause state

    def on_press(self, key):
        try:
            if key == keyboard.Key.f6:  # toggle pause/start
                self.pause = not self.pause
                print("⏸ Paused" if self.pause else "▶ Running")
            elif key == keyboard.Key.f7:  # exit program
                self.pause = True
                stop_event.set()  # signal all threads to stop
                print("❌ Exit")
                return False
        except:
            pass

    def run(self):
        # Main clicker loop
        while not stop_event.is_set():
            if not self.pause:
                pyautogui.click(button=self.button)
                time.sleep(self.click_cooldown)
            else:
                time.sleep(0.1)

def start_ui():
    UI = ClickerUI()

    def on_close():
        stop_event.set()  # stop everything when GUI is closed
        UI.root.destroy()

    UI._ui_init()
    UI.root.protocol("WM_DELETE_WINDOW", on_close)

    # Periodically check if stop_event is set
    def check_stop():
        if stop_event.is_set():
            UI.root.destroy()
        else:
            UI.root.after(100, check_stop)

    UI.root.after(100, check_stop)
    UI.root.mainloop()

if __name__ == "__main__":
    # Start clicker
    clicker = Clicker()
    listener = keyboard.Listener(on_press=clicker.on_press)
    listener.start()

    clicker_thread = threading.Thread(target=clicker.run, daemon=True)
    clicker_thread.start()

    # Start GUI
    start_ui()