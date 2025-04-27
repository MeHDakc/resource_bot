import unittest
from unittest.mock import patch
from app.game_actions import exit_city, search_resources_interface


class TestGameActions(unittest.TestCase):
    @patch("app.game_actions.exit_city")
    def test_exit_city(self, mock_exit_city):
        mock_exit_city.return_value = None
        try:
            exit_city()
        except RuntimeError as e:
            self.fail(f"exit_city() raised RuntimeError unexpectedly: {e}")

    @patch("app.game_actions.search_resources_interface")
    def test_search_resources_interface(self, mock_search_resources_interface):
        mock_search_resources_interface.return_value = None
        try:
            search_resources_interface()
        except RuntimeError as e:
            self.fail(
                f"search_resources_interface() raised RuntimeError unexpectedly: {e}"
            )


if __name__ == "__main__":
    unittest.main()
