from app.game_actions import exit_city, search_resources_interface
import time
import random

if __name__ == "__main__":
    try:
        print("Testing exit_city()...")
        exit_city()
        print("Exit city action executed successfully.")

        time.sleep(random.uniform(1, 3))

        print("Testing search_resources_interface()...")
        search_resources_interface()
        print("Search resources action executed successfully.")
    except RuntimeError as e:
        print(f"Error: {e}")
