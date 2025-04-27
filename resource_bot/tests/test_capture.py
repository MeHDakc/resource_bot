import unittest
from unittest.mock import patch
from app.capture import capture_screen


class TestCapture(unittest.TestCase):
    @patch("app.capture.cv2.imwrite")
    @patch("app.capture.cv2.cvtColor")
    @patch("app.capture.pyautogui.screenshot")
    def test_capture_screen(self, mock_screenshot, mock_cvtcolor, mock_imwrite):
        mock_screenshot.return_value = "fake_image"
        mock_cvtcolor.return_value = "processed_image"
        mock_imwrite.return_value = True

        result = capture_screen("test.png")
        self.assertTrue(result)
        mock_screenshot.assert_called_once()
        mock_cvtcolor.assert_called_once_with("fake_image", 4)
        mock_imwrite.assert_called_once_with("test.png", "processed_image")


if __name__ == "__main__":
    unittest.main()
