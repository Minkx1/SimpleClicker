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
        self.root.geometry("340x260")
        self.root.resizable(False, False)

        # Info label with hotkeys
        self.label_info = ctk.CTkLabel(
            self.root,
            text="F6 — Start/Stop Clicker | F7 — Exit Program",
            font=("Arial", 12)
        )
        self.label_info.pack(pady=(10,5))

        frame = ctk.CTkFrame(self.root)
        frame.pack(fill="both", expand=True, padx=15, pady=15)

        # Clicks per second input
        self.label_cps = ctk.CTkLabel(frame, text="Clicks/sec")
        self.label_cps.pack(anchor="w", pady=(5, 0))

        self.entry_cps = ctk.CTkEntry(frame)
        self.entry_cps.insert(0, str(self.base_cps))
        self.entry_cps.pack(fill="x", pady=(0, 10))

        # Mouse button selection
        self.label_button = ctk.CTkLabel(frame, text="Mouse Button")
        self.label_button.pack(anchor="w", pady=(5, 0))

        self.combo_button = ctk.CTkOptionMenu(frame, values=["left", "right", "middle"])
        self.combo_button.set(self.base_button)
        self.combo_button.pack(fill="x", pady=(0, 10))  

        # Save button
        ctk.CTkButton(frame, text="Save Changes", command=self.save_settings).pack(pady=10)


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
