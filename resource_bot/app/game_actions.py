import pyautogui
import time
import random
from app.detector.opencv_detector import find_button_on_screen


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
