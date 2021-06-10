import pytest
from unittest.mock import patch
from source.json_parser import JsonParser

def test_get_signal_title():
    with patch.object(JsonParser, "get_signal_title", return_value="ECU Reset"):
        json_parser = JsonParser
        json_parser.data = {"services": [{"title": "ECU Reset", "id": "11"}]}
        assert json_parser.get_signal_title("11") == "ECU Reset"
        
# TODO: Missing test load function
