from app.detector.opencv_detector import find_resource_on_screen

if __name__ == "__main__":
    resource_type = "wood"
    try:
        location = find_resource_on_screen(resource_type)
        if location:
            print(f"Resource '{resource_type}' found on locatin: {location}")
        else:
            print(f"Resource '{resource_type}' not found.")
    except FileNotFoundError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")
