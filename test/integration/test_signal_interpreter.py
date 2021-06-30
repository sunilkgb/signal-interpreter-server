from source.main import main
from source import router
from source.json_parser import JsonParser
import pytest
from unittest.mock import patch
import sys


def test_get_signal_title(json_parser_instance):
    json_parser=JsonParser()
    json_parser.data=json_parser_instance.data
    assert json_parser.get_signal_title("10") == "ECU Reset"


# @pytest.mark.parametrize("payload, expected_status_code, expected_response", [
#     ({"signal": "11"}, 200, "ECU Reset"),
#     ({"signal": "27"}, 400, "Security Access")
# ])
# @patch.object(sys, "argv", ["program_name", "--file_path","test/integration/fixtures/test_basic.json"])
# def test_signal_interpreter_app(payload, expected_status_code, expected_response, json_parser_instance, test_client_function):
#     with patch.object(router.my_signal_interpreter_app, "run"):
#         with test_client_function as client:
#             main()
#             json_parser = JsonParser
#             # assert json_parser.load_file(file_path) == json_parser_instance.data
#             response = client.post("/", json=payload)
#             assert response.get_json() == expected_response



@pytest.mark.parametrize("payload, expected_status_code, expected_response", [
    ({"signal": "11"}, 200, "ECU Reset"),
    ({"signal": "27"}, 400, "Security Access")
])
@patch.object(sys, "argv", ["program_name", "--file_path","test/integration/fixtures/test_basic.json"])
@patch.object(router.my_signal_interpreter_app, "run")
def test_signal_interpreter_app(a, payload, expected_status_code, expected_response, test_client_function):
    with test_client_function as client:
        main()
        response = client.post("/", json=payload)
        assert response.get_json() == expected_response


#     #json_parser.load_file(args.file_path)
#     #router.my_signal_interpreter_app.run()


#     ##mock signal interpreter app
#     ## mock start of the app
#     ## add some classes inititations in contest.py

#     ## Above is the wrong approach , you need to write test cases for each function from end to end using the same data in fixtures and contest,py
#     ## example test_get_signal_title, test_my_signal_interpreter_app.run , starting the client