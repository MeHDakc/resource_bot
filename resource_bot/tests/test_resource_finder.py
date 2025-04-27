import unittest
from unittest.mock import patch
from app.resource_finder import find_resource


class TestResourceFinder(unittest.TestCase):
    @patch("app.resource_finder.find_button_on_screen")
    def test_find_resource(self, mock_find_button_on_screen):
        mock_find_button_on_screen.return_value = (150, 250)

        location = find_resource("gold.png")
        self.assertEqual(location, (150, 250))
        mock_find_button_on_screen.assert_called_once_with("gold.png", threshold=0.8)


if __name__ == "__main__":
    unittest.main()
