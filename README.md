# CS2 Nine Out Of Ten 

A lightweight, Python-based utility that uses Computer Vision to detect the Counter-Strike 2 "ACCEPT" button and allows you to accept matches automaticlly 

Since this script relies entirely on screen capture and OS-level mouse emulation—without reading game memory or injecting any code—it is **completely safe and carries no VAC ban risk**.

## ✨ Features
* **Computer Vision (OpenCV):** Detects the exact green color of the ACCEPT button, ignoring monitor brightness or digital vibrance settings.
* **Resolution Independent:** Automatically detects your primary monitor's resolution and calculates the center, working perfectly with native (16:9) or stretched (4:3) resolutions.
* **Smart Polling:** Takes screenshots efficiently in RAM (using `mss`) to avoid disk wear and CPU overhead.

## 🛠️ Prerequisites
* **Python 3.8** or higher installed on your system.
* **Counter-Strike 2** running on your primary monitor (Fullscreen Windowed or Windowed mode is recommended for seamless alt-tabbing, but Fullscreen works as well).

## 🚀 Installation

1. **Clone or download** this repository to your local machine.
2. **Open a terminal in the project directory.**
3. **Install the required dependencies** by running the following command in your terminal:
```bash
pip install -r requirements.txt 
```

4. **Run the script:**
```bash
py main.py
```

5. **Start searching for a competitive match in CS2.**

You can now walk away from your PC. When a match is found, the script will automatically move your mouse and click the accept button in-game.

To stop the script manually at any time, press Ctrl-C on your keyboard.

⚠️ Disclaimer
This tool uses pydirectinput to simulate hardware-level mouse clicks and mss for screen capture. It does not interact with the CS2 game engine or memory in any way. It provides no in-game advantages and only operates in the main menu lobby. Use it responsibly.
