import cv2
import numpy as np
import os
from app.capture import capture_screen
from typing import Optional, Tuple

ASSETS_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), "..", "assets")
BUTTONS_DIR = os.path.join(
    os.path.dirname(os.path.dirname(__file__)), "..", "assets", "buttons"
)


def find_resource_on_screen(
    resource_type: str, threshold: float = 0.8
) -> Optional[Tuple[int, int]]:
    screenshot_path = capture_screen()
    if not os.path.exists(screenshot_path):
        raise FileNotFoundError(f"Screenshot not found at {screenshot_path}")

    screenshot_rgb = cv2.imread(screenshot_path)
    if screenshot_rgb is None:
        raise ValueError(f"Failed to load screenshot from {screenshot_path}")

    screenshot_gray = cv2.cvtColor(screenshot_rgb, cv2.COLOR_BGR2GRAY)
    os.remove(screenshot_path)

    template_path = os.path.join(ASSETS_DIR, f"{resource_type}.png")
    template = cv2.imread(template_path, cv2.IMREAD_GRAYSCALE)
    if template is None:
        raise FileNotFoundError(
            f"Resource template {resource_type}.png not found in assets."
        )

    result = cv2.matchTemplate(screenshot_gray, template, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

    if max_val >= threshold:
        return max_loc
    return None


def find_button_on_screen(
    button_name: str, threshold: float = 0.8
) -> Optional[Tuple[int, int]]:
    screenshot_path = capture_screen()
    if not os.path.exists(screenshot_path):
        raise FileNotFoundError(f"Screenshot not found at {screenshot_path}")

    screenshot_rgb = cv2.imread(screenshot_path)
    if screenshot_rgb is None:
        raise ValueError(f"Failed to load screenshot from {screenshot_path}")

    screenshot_gray = cv2.cvtColor(screenshot_rgb, cv2.COLOR_BGR2GRAY)
    os.remove(screenshot_path)
    template_path = os.path.join(BUTTONS_DIR, f"{button_name}.png")
    template = cv2.imread(template_path, cv2.IMREAD_GRAYSCALE)
    if template is None:
        raise FileNotFoundError(
            f"Resource template {button_name}.png not found in assets."
        )

    result = cv2.matchTemplate(screenshot_gray, template, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

    if max_val >= threshold:
        return max_loc
    return None
