from unittest.mock import patch
import pytest
from source.router import my_signal_interpreter_app
from source.json_parser import JsonParser


def test_my_routes_function():
    my_signal_interpreter_app.testing = True
    my_signal_interpreter_app_instance = my_signal_interpreter_app.test_client()
    
    with my_signal_interpreter_app_instance as client:
        with patch.object(JsonParser, "get_signal_title", return_value = "ECU Reset"):
            my_payload = {"signal":"36"}
            response = client.post("/", json=my_payload)
            assert response.get_json() == "ECU Reset"