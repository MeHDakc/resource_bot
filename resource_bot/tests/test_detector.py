import unittest
from unittest.mock import patch
from app.detector.opencv_detector import find_button_on_screen


class TestDetector(unittest.TestCase):
    @patch("app.detector.opencv_detector.cv2.matchTemplate")
    @patch("app.detector.opencv_detector.cv2.minMaxLoc")
    @patch("app.detector.opencv_detector.capture_screen")
    def test_find_button_on_screen(
        self, mock_capture_screen, mock_minmaxloc, mock_matchtemplate
    ):
        mock_capture_screen.return_value = "screen_image"
        mock_matchtemplate.return_value = "result_matrix"
        mock_minmaxloc.return_value = (None, 0.9, None, (100, 200))

        location = find_button_on_screen("button.png", threshold=0.8)
        self.assertEqual(location, (100, 200))
        mock_capture_screen.assert_called_once()
        mock_matchtemplate.assert_called_once_with("screen_image", "button.png", 5)
        mock_minmaxloc.assert_called_once()


if __name__ == "__main__":
    unittest.main()
