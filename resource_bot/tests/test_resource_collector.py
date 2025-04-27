import unittest
from unittest.mock import patch
from app.resource_collector import search_and_collect_resource


class TestResourceCollector(unittest.TestCase):
    @patch("app.resource_collector.find_button_on_screen")
    @patch("app.resource_collector.find_resource_on_screen")
    @patch("app.resource_collector.click_button")
    def test_search_and_collect_resource_success(
        self,
        mock_click_button,
        mock_find_resource_on_screen,
        mock_find_button_on_screen,
    ):
        # Mock button and resource locations
        mock_find_button_on_screen.side_effect = [
            (100, 200),  # Resource button found
            (300, 400),  # SEARCH button found
        ]
        mock_find_resource_on_screen.return_value = (500, 600)  # Resource found

        # Call the function
        search_and_collect_resource("Cropland")

        # Assertions
        self.assertEqual(mock_find_button_on_screen.call_count, 2)
        mock_find_button_on_screen.assert_any_call("Cropland", threshold=0.8)
        mock_find_button_on_screen.assert_any_call("SEARCH", threshold=0.8)

        mock_click_button.assert_any_call("Cropland")
        mock_click_button.assert_any_call("SEARCH")
        mock_click_button.assert_any_call((500, 600))

    @patch("app.resource_collector.find_button_on_screen")
    def test_search_and_collect_resource_no_resource_button(
        self, mock_find_button_on_screen
    ):
        # Mock resource button not found
        mock_find_button_on_screen.return_value = None

        with self.assertRaises(
            RuntimeError, msg="Button for resource 'Cropland' not found."
        ):
            search_and_collect_resource("Cropland")

    @patch("app.resource_collector.find_button_on_screen")
    @patch("app.resource_collector.find_resource_on_screen")
    def test_search_and_collect_resource_no_search_button(
        self, mock_find_resource_on_screen, mock_find_button_on_screen
    ):
        # Mock resource button found, but SEARCH button not found
        mock_find_button_on_screen.side_effect = [
            (100, 200),  # Resource button found
            None,  # SEARCH button not found
        ]

        with self.assertRaises(RuntimeError, msg="'SEARCH' button not found."):
            search_and_collect_resource("Cropland")

    @patch("app.resource_collector.find_button_on_screen")
    @patch("app.resource_collector.find_resource_on_screen")
    @patch("app.resource_collector.click_button")
    def test_search_and_collect_resource_no_resource_found(
        self,
        mock_click_button,
        mock_find_resource_on_screen,
        mock_find_button_on_screen,
    ):
        # Mock buttons found but no resource found
        mock_find_button_on_screen.side_effect = [
            (100, 200),  # Resource button found
            (300, 400),  # SEARCH button found
        ]
        mock_find_resource_on_screen.return_value = None  # No resource found

        search_and_collect_resource("Cropland")

        # Assertions
        self.assertEqual(mock_find_button_on_screen.call_count, 2)
        mock_find_button_on_screen.assert_any_call("Cropland", threshold=0.8)
        mock_find_button_on_screen.assert_any_call("SEARCH", threshold=0.8)

        mock_click_button.assert_any_call("Cropland")
        mock_click_button.assert_any_call("SEARCH")
        mock_click_button.assert_not_called_with((500, 600))


if __name__ == "__main__":
    unittest.main()
