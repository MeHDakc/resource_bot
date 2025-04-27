from app.game_actions import smart_drag_slider
from app.detector.opencv_detector import find_slider


def set_slider_to_max():
    slider = find_slider("slider_image", threshold=0.8)
    if not slider:
        raise RuntimeError("Slider bar not found.")

    slider_start = (slider[0] + 10, slider[1] + slider[3] // 2)
    slider_end = (slider[0] + slider[2] - 10, slider_start[1])

    smart_drag_slider(slider_start, slider_end, duration=1.0)
    print("Slider moved to maximum position.")
