# SimpleClicker

SimpleClicker is a lightweight and customizable auto-clicker for Windows, built with Python. It allows you to automate different mouse clicks with configurable clicks per second (CPS), mouse button selection, different modes of clicking and hotkeys.

The newest version is 1.0.0
---

## Features

- **Custom CPS**: Set the number of clicks per second.
- **Mouse Button Selection**: Choose left, right, or middle mouse button.
<<<<<<< HEAD
- **Customizable Hotkeys**:
  - **F6** — Start/Stop clicker (by default)
  - **F7** — Exit program (by default)
=======
- **Hotkeys**:
  - **F6** — Start/Stop clicker
  - **F7** — Exit program
>>>>>>> 31dbb2d57144ca1fcfd76e942e770964e6a2c549
- **Settings Persistence**: Configuration is saved in `AppData/Roaming/SimpleClicker/settings.json`.
- **Custom UI**: Built with [CustomTkinter](https://github.com/TomSchimansky/CustomTkinter) for a modern dark theme interface.

---

## Installation

There is 2 ways to install. 

1. Clone the repository and install dependencies:

```bash
git clone https://github.com/Minkx1/SimpleClicker.git
cd SimpleClicker
````
```bash
pip install -r requirements.txt
```

2. Download built EXE file:
  - `SimpleClicker.exe`

## Usage

Run the python `main` file:

```bash
python main.py
```
Or run .exe file.

1. Set your desired **Clicks/sec**, **Mouse Button** and **Click Mode** in the GUI.
2. Use **F6** or configured hotkey to start or stop the clicker.
3. Use **F7** or configured hotkey or close the window to exit the program.

Settings will be automatically saved.

---

## License

This Project is free to use. Not for a comercial.

---

## Notes

* Works only on **Windows** (uses `%APPDATA%` for settings folder).
* Make sure your Python environment has required packages installed.

---
