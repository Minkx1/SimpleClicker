# SimpleClicker

SimpleClicker is a lightweight and customizable auto-clicker for Windows, built with Python. It allows you to automate mouse clicks with configurable clicks per second (CPS), mouse button selection, and hotkeys.

---

## Features

- **Custom CPS**: Set the number of clicks per second.
- **Mouse Button Selection**: Choose left, right, or middle mouse button.
- **Hotkeys**:
  - **F6** — Start/Stop clicker
  - **F7** — Exit program
- **Settings Persistence**: Configuration is saved in `AppData/SimpleClicker/settings.json`.
- **Custom UI**: Built with [CustomTkinter](https://github.com/TomSchimansky/CustomTkinter) for a modern dark theme interface.

---

## Installation

1. Clone the repository:

```bash
git clone https://github.com/yourusername/SimpleClicker.git
cd SimpleClicker
````

2. Install dependencies:

```bash
pip install -r requirements.txt
```

**Dependencies:**

* `pyautogui`
* `pynput`
* `customtkinter`

---

## Usage

Run the program:

```bash
python main.py
```

1. Set your desired **Clicks/sec** and **Mouse Button** in the GUI.
2. Use **F6** to start or stop the clicker.
3. Use **F7** or close the window to exit the program.

Settings will be automatically saved.

---

## File Structure

```
SimpleClicker/
├── main.py           # Main program, runs UI and clicker
├── UI.py             # GUI code using CustomTkinter
├── settings.py       # Settings management with JSON persistence
├── README.md         # This file
└── requirements.txt  # Python dependencies
```

---

## License

MIT License. See `LICENSE` file for details.

---

## Notes

* Works only on **Windows** (uses `%APPDATA%` for settings folder).
* Make sure your Python environment has required packages installed.
* Hotkeys (`F6`/`F7`) are global and work while the program is running.

---
