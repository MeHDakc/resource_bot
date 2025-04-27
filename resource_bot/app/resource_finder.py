from app.game_actions import exit_city, search_resources_interface
from app.detector.opencv_detector import find_resource_on_screen


def find_and_gather_resource(preferred_resources: list):
    exit_city()
    for resource in preferred_resources:
        for level in range(8, 4, -1):
            search_resources_interface()
            location = find_resource_on_screen(resource)
            if location:
                return location
    return None
