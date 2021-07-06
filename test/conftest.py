import pytest
from source.json_parser import JsonParser
from source.router import my_signal_interpreter_app
from source.xml_parser import XmlParser


@pytest.fixture
def json_parser_instance():
    json_parser_instance = JsonParser()
    json_parser_instance.data = {
    "services": [
        {
            "title": "ECU Reset",
            "id": "11"
        },
        {
            "title": "Security Access",
            "id": "27"
        }]}
    return json_parser_instance

@pytest.fixture
def test_client_function():
    my_signal_interpreter_app.testing = True
    return  my_signal_interpreter_app.test_client()

@pytest.fixture
def xml_parser_instance():
    xml_parser = XmlParser()
    xml_parser.data = {"services": {"service": [{"title": "ECU Reset", "@id": "11"}]}}
    return xml_parser
