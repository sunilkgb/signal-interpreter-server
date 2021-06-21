import pytest
from unittest.mock import patch, mock_open
from source.json_parser import JsonParser


def test_load_file():
    with patch("builtins.open", mock_open(read_data='{ "json" : "ECU Reset" }')):
        json_parser = JsonParser()
        json_parser.load_file("path/to/json/file")
        assert json_parser.data == {"json": "ECU Reset"}

@pytest.mark.parametrize("signal, title", 
[("27", "Security Access"),("11", "ECU Reset")])
def test_get_signal_title(signal, title):
    json_parser = JsonParser()
    json_parser.data = {
    "services": [
        {
            "title": "ECU Reset",
            "id": "11"
        },
        {
            "title": "Security Access",
            "id": "27"
        },
        {
            "title": "Tester Present",
            "id": "3E"
        },
        {
            "title": "Request Download",
            "id": "34"
        },
        {
            "title": "Transfer Data",
            "id": "36"
        }
    ]
}
    assert json_parser.get_signal_title(signal) == title


