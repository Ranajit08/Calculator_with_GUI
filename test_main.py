from unittest.mock import patch
import main


@patch("main.gui")
def test_main(mock_gui):
    main.main()
    mock_gui.assert_called_once()
