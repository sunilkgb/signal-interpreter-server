from unittest.mock import patch
import pytest
from source.router import my_signal_interpreter_app, parser_factory
from source.json_parser import JsonParser


def test_my_routes_function():
    my_signal_interpreter_app.testing = True
    my_signal_interpreter_app_instance = my_signal_interpreter_app.test_client()
    
    with my_signal_interpreter_app_instance as client:
        with patch.object(JsonParser, "get_signal_title", return_value = "ECU Reset") as mock_get_signal_title :
            with patch.object(parser_factory, "get_parser", return_value=JsonParser):
                my_payload = {"signal":"36"}
                response = client.post("/", json=my_payload)
                # mock_get_signal_title.assert_called_with("36")
                assert response.get_json() == "ECU Reset"

# def test_interpret_signal(payload, expected_status_code, expected_response, signal_interpreter_app_instance):
#     with signal_interpreter_app_instance as client:
#         with patch.object(JsonParser, "get_signal_title", return_value=expected_response):
#             with patch.object(parser_factory, "get_parser", return_value=JsonParser):
#                 response = client.post("/", json=payload)
#                 assert response.get_json() == expected_response
#                 assert response.status_code == expected_status_code