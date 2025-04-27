from app.capture import capture_screen

if __name__ == "__main__":
    path = capture_screen()
    print(f"Тест: Скриншот сохранён в {path}")
