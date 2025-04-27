import cv2
import numpy as np
import os
from app.capture import capture_screen
from typing import Optional, Tuple

ASSETS_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), "..", "assets")
BUTTONS_DIR = os.path.join(
    os.path.dirname(os.path.dirname(__file__)), "..", "assets", "buttons"
)


def capture_and_find(
    template_path: str, threshold: float = 0.8
) -> Optional[Tuple[int, int]]:
    screenshot_path = capture_screen()
    try:
        screenshot = cv2.imread(screenshot_path, cv2.IMREAD_GRAYSCALE)
        if screenshot is None:
            raise ValueError("Failed to load screenshot.")

        template = cv2.imread(template_path, cv2.IMREAD_GRAYSCALE)
        if template is None:
            raise FileNotFoundError(f"Template not found: {template_path}")

        result = cv2.matchTemplate(screenshot, template, cv2.TM_CCOEFF_NORMED)
        _, max_val, _, max_loc = cv2.minMaxLoc(result)

        if max_val >= threshold:
            h, w = template.shape[:2]
            return max_loc[0], max_loc[1], w, h
        return None
    finally:
        if os.path.exists(screenshot_path):
            os.remove(screenshot_path)


def find_resource_on_screen(
    resource_type: str, threshold: float = 0.8
) -> Optional[Tuple[int, int]]:
    template_path = os.path.join(ASSETS_DIR, f"{resource_type}.png")
    return capture_and_find(template_path, threshold)


def find_button_on_screen(
    button_name: str, threshold: float = 0.8
) -> Optional[Tuple[int, int]]:
    template_path = os.path.join(BUTTONS_DIR, f"{button_name}.png")
    return capture_and_find(template_path, threshold)


def find_slider(
    slider_name: str, threshold: float = 0.8
) -> Optional[Tuple[int, int, int, int]]:
    template_path = os.path.join(BUTTONS_DIR, f"{slider_name}.png")
    return capture_and_find(template_path, threshold)
