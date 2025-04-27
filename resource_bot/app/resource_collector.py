from app.detector.opencv_detector import find_button_on_screen, find_resource_on_screen
from app.game_actions import click_button
import time


def search_and_collect_resource(resource_type: str):
    button_location = find_button_on_screen(resource_type, threshold=0.8)
    if button_location:
        click_button(resource_type)
        time.sleep(1)
    else:
        raise RuntimeError(f"Button for resource '{resource_type}' not found.")

    search_button = find_button_on_screen("SEARCH", threshold=0.8)
    if search_button:
        click_button("SEARCH")
        time.sleep(2)
    else:
        raise RuntimeError("'SEARCH' button not found.")

    for attempt in range(3):
        resource_location = find_resource_on_screen(resource_type.lower())
        if resource_location:
            click_button(resource_location)
            print(f"Collecting resource '{resource_type}'.")
            return
        else:
            print(
                f"Attempt {attempt+1}: Resource '{resource_type}' not found, retrying..."
            )
            time.sleep(1)

    print(f"Resource '{resource_type}' was not found after multiple attempts.")

    # Select resource type
    button_location = find_button_on_screen(resource_type, threshold=0.8)
    if button_location:
        click_button(resource_type)
        time.sleep(1)
    else:
        raise RuntimeError(f"Button for resource '{resource_type}' not found.")

    # Click SEARCH button
    search_button = find_button_on_screen("SEARCH", threshold=0.8)
    if search_button:
        click_button("SEARCH")
        time.sleep(2)
    else:
        raise RuntimeError("'SEARCH' button not found.")

    # Locate and collect resource
    resource_location = find_resource_on_screen(resource_type.lower())
    if resource_location:
        click_button(resource_location)
        print(f"Collecting resource '{resource_type}'.")
    else:
        print(f"Resource '{resource_type}' not found.")
