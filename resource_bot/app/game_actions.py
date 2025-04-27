import pyautogui
import time
import random
from app.detector.opencv_detector import find_button_on_screen
from typing import Tuple


def click_button(button_name: str):

    location = find_button_on_screen(button_name, threshold=0.8)
    if location:
        pyautogui.click(location)
        time.sleep(random.uniform(0.5, 1.5))
    else:
        raise RuntimeError(f"Button '{button_name}' not found on the screen.")


def exit_city():

    if random.choice([True, False]):
        click_button("exit_city")
    else:
        pyautogui.press("space")
        time.sleep(random.uniform(1, 3))


def search_resources_interface():
    time.sleep(random.uniform(1, 2))
    if random.choice([True, False]):
        click_button("search_resources")
    else:
        pyautogui.press("B")
        time.sleep(random.uniform(0.5, 1.5))


def smart_drag_slider(
    start_position: Tuple[int, int], end_position: Tuple[int, int], duration=1.0
):

    steps = random.randint(20, 40)
    x_start, y_start = start_position
    x_end, y_end = end_position

    pyautogui.moveTo(x_start, y_start, duration=random.uniform(0.1, 0.2))
    pyautogui.mouseDown()

    for step in range(steps):
        progress = step / steps
        x = int(x_start + (x_end - x_start) * progress + random.uniform(-2, 2))
        y = int(y_start + (y_end - y_start) * progress + random.uniform(-2, 2))
        pyautogui.moveTo(x, y, duration=random.uniform(0.01, 0.03))

    pyautogui.moveTo(x_end, y_end, duration=random.uniform(0.05, 0.1))
    pyautogui.mouseUp()
