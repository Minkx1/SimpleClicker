"""===== UI.py ====="""

from settings import *

import customtkinter as ctk
from tkinter import messagebox
from pynput import keyboard

class ClickerUI():
    def __init__(self):
        # Load initial settings
        self.base_cps = get_setting('cps')
        self.base_button = get_setting('mouse_button')

    def _ui_init(self):
        ctk.set_appearance_mode("dark")        # "light" or "dark"
        ctk.set_default_color_theme("blue")    # color theme

        self.root = ctk.CTk()
        self.root.title(f"SimpleClicker V{version}")
        self.root.geometry("640x320") 
        self.root.resizable(False, False)

        # Info label with hotkeys
        hotkey_start = get_setting('hotkey_start')
        hotkey_quit = get_setting('hotkey_quit')
        self.label_info = ctk.CTkLabel(
            self.root,
            text=f"{hotkey_start} — Start/Stop Clicker | {hotkey_quit} — Exit Program",
            font=("Arial", 15)
        )
        self.label_info.pack(pady=(10,5))

        frame = ctk.CTkFrame(self.root)
        frame.pack(fill="both", expand=True, padx=15, pady=15)

        # Main Buttons
        left_frame = ctk.CTkFrame(frame)
        left_frame.pack(side="left", fill="both", expand=True, padx=(0,10))

        self.label_cps = ctk.CTkLabel(left_frame, text="Clicks/sec")
        self.label_cps.pack(anchor="w", pady=(5, 0))

        self.entry_cps = ctk.CTkEntry(left_frame)
        self.entry_cps.insert(0, str(self.base_cps))
        self.entry_cps.pack(fill="x", pady=(0, 10))

        self.label_button = ctk.CTkLabel(left_frame, text="Mouse Button")
        self.label_button.pack(anchor="w", pady=(5, 0))

        self.combo_button = ctk.CTkOptionMenu(left_frame, values=["left", "right", "middle"])
        self.combo_button.set(self.base_button)
        self.combo_button.pack(fill="x", pady=(0, 10))  

        ctk.CTkButton(left_frame, text="Save Changes", command=self.save_settings).pack(pady=10)

        # HotKeys Buttons and Clicker Mode
        right_frame = ctk.CTkFrame(frame)
        right_frame.pack(side="right", fill="both", expand=False)

        self.btn_start_hotkey = ctk.CTkButton(
            right_frame,
            text=f"Set Start Hotkey ({get_setting('hotkey_start')})",
            command=self.set_start_hotkey
        )
        self.btn_start_hotkey.pack(pady=(20,10), padx=10, fill="x")

        self.btn_quit_hotkey = ctk.CTkButton(
            right_frame,
            text=f"Set Quit Hotkey ({get_setting('hotkey_quit')})",
            command=self.set_quit_hotkey
        )
        self.btn_quit_hotkey.pack(pady=(10,20), padx=10, fill="x")

        # Clicker mode selection
        mode_frame = ctk.CTkFrame(right_frame)
        mode_frame.pack(anchor="ne", pady=(5, 0))

        self.label_mode = ctk.CTkLabel(mode_frame, text="Clicker Mode")
        self.label_mode.pack(side="left", padx=(0, 5))

        self.combo_mode = ctk.CTkOptionMenu(
            mode_frame,
            values=["single", "double", "hold"],
            command= lambda choice: set_setting('clicker_mode', choice)
        )
        self.combo_mode.set(get_setting("clicker_mode"))
        self.combo_mode.pack(side="left")


    def set_start_hotkey(self):
        self._listen_for_hotkey('hotkey_start')

    def set_quit_hotkey(self):
        self._listen_for_hotkey('hotkey_quit')
    
    def update_hotkey_label(self):
        hotkey_start = get_setting('hotkey_start')
        hotkey_quit = get_setting('hotkey_quit')
        self.label_info.configure(text=f"{hotkey_start} — Start/Stop Clicker | {hotkey_quit} — Exit Program")

    def _listen_for_hotkey(self, key_name):
        overlay = ctk.CTkToplevel(self.root)
        overlay.attributes('-fullscreen', True)
        overlay.attributes('-alpha', 0.5)
        overlay.configure(bg='black')
        overlay.focus_set()

        label = ctk.CTkLabel(overlay, text="Press any key...", font=("Arial", 20))
        label.pack(expand=True)

        def on_press(key):
            try:
                if hasattr(key, 'char') and key.char:
                    k = key.char.upper()
                elif hasattr(key, 'vk') and 96 <= key.vk <= 105:
                    # NumPad 0..9
                    k = f"NUMPAD{key.vk - 96}"
                else:
                    k = str(key).replace("Key.", "").upper()
                set_setting(key_name, k)

                # Виклик destroy та UI оновлення у головному потоці
                overlay.after(0, overlay.destroy)
                
                if key_name == 'hotkey_start':
                    self.root.after(0, lambda: self.btn_start_hotkey.configure(text=f"Set Start Hotkey ({k})"))
                elif key_name == 'hotkey_quit':
                    self.root.after(0, lambda: self.btn_quit_hotkey.configure(text=f"Set Quit Hotkey ({k})"))
                
                self.update_hotkey_label()
                
                return False
            except Exception as e:
                print(e)
                overlay.after(0, overlay.destroy)
                return False

        listener = keyboard.Listener(on_press=on_press)
        listener.start()

    def save_settings(self):
        try:
            cps = int(self.entry_cps.get())
            if cps <= 0:
                raise ValueError
            self.base_cps = cps
        except ValueError:
            # Show error if input is invalid
            messagebox.showerror("Error", "Please enter a valid positive number for Clicks/sec.")
            self.entry_cps.delete(0, "end")
            self.entry_cps.insert(0, str(self.base_cps))
            return

        # Save values from fields to settings
        self.base_button = self.combo_button.get()
        set_setting('mouse_button', self.base_button)
        set_setting('cps', self.base_cps)

        # Updating UI
        self.entry_cps.delete(0, "end")
        self.entry_cps.insert(0, str(self.base_cps))
        self.combo_button.set(self.base_button)
        clicker_mode = self.combo_mode.get()
        set_setting("clicker_mode", clicker_mode)
    
    def run(self,stop_event=None):
        if stop_event!=None:
            def on_close():
                stop_event.set()  # stop everything when GUI is closed
                self.root.destroy()

            self._ui_init()
            self.root.protocol("WM_DELETE_WINDOW", on_close)

            # Periodically check if stop_event is set
            def check_stop():
                if stop_event.is_set():
                    self.root.destroy()
                else:
                    self.root.after(100, check_stop)

            self.root.after(100, check_stop)
            self.root.mainloop()
        else: 
            self._ui_init()
            self.root.mainloop()

# UI = ClickerUI()
# UI.run()
