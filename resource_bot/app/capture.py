import pyautogui
import os
from datetime import datetime
from config.settings import CAPTURE_DIR


def capture_screen(save_dir=CAPTURE_DIR):
    os.makedirs(save_dir, exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    file_path = os.path.join(save_dir, f"screenshot_{timestamp}.png")
    screenshot = pyautogui.screenshot()
    screenshot.save(file_path)
    return file_path
