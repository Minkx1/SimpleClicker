import pyautogui
import time
from pynput import keyboard

CLICK_COOLDOWN = 0.01 # час між кілками в секундах.
BUTTON = 'left'

class Clicker():
    def __init__(self):
        self.pause = True
        self.running = True
    def on_press(self, key):
        try:
            if key == keyboard.Key.f6:  # Запустити/зупинити клікер
                self.pause = not self.pause
                print("⏸ Зупинено" if self.pause else "▶ Запущено")
            elif key == keyboard.Key.f7:  # Вийти з програми
                self.pause = True
                self.running = False
                print("❌ Вихід")
                return False
        except:
            pass
    def run(self):
        while (self.running):
            if not (self.pause):
                pyautogui.click(button=BUTTON)
                time.sleep(CLICK_COOLDOWN)
            else:
                time.sleep(0.1)

clck = Clicker()

print("F6 — старт/стоп клікеру | F7 — вихід з програми")

listener = keyboard.Listener(on_press=clck.on_press)
listener.start()

clck.run()