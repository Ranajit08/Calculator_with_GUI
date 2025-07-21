import unittest
from unittest.mock import patch
import main


class Testmain(unittest.TestCase):
    @patch("main.gui")
    def test_main(self, mock_gui):
        main.main()
        mock_gui.assert_called_once()


if __name__ == "__main__":
    unittest.main()
