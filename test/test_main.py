""" Unit tests for main.py """
# pylint: disable=missing-function-docstring, missing-class-docstring
import pytest
from unittest.mock import patch
from source.main import parse_argument, ArgumentParser,main, init
from source.main import parser_factory, load_signal_database_file, register_all_parsers
from source import router
from source.json_parser import JsonParser
from source.xml_parser import XmlParser


class MockArgs: # pylint: disable=too-few-public-methods
    file_path = "path/to/file"

@patch.object(ArgumentParser,"add_argument")
@patch.object(ArgumentParser,"parse_args",return_value=MockArgs)
def test_parse_argument(mock_parse_args,mock_add_argument):
     assert parse_argument() == MockArgs
     mock_parse_args.assert_called_once()
     mock_add_argument.assert_called_with("--file_path")

# @patch("source.main.parse_argument", return_value=MockArgs)
# @patch.object(JsonParser, "load_file")
# @patch.object(router.my_signal_interpreter_app, "run")
# def test_main(mock_signal_interpreter_app_run, mock_load_file, mock_parse_args):
#     main()
#     mock_parse_args.assert_called_once()
#     mock_load_file.assert_called_with(MockArgs.file_path)
#     mock_signal_interpreter_app_run.assert_called_once()


def test_register_all_parsers():
    with patch.object(parser_factory, "register_format") as mock_register_parser:
        register_all_parsers()
        mock_register_parser.assert_called()


def test_load_signal_database_file():
    with patch.object(parser_factory, "set_signal_database_format") as mock_set_signal_database_format:
        with patch.object(JsonParser, "load_file") as mock_load_file:
            with patch.object(parser_factory, "get_parser", return_value=JsonParser) as mock_get_parser:
                load_signal_database_file("json", "file_path.json")
                mock_set_signal_database_format.assert_called_once()
                mock_set_signal_database_format.assert_called_with("json")
                mock_get_parser.assert_called_once()
                mock_load_file.assert_called_with("file_path.json")


@patch.object(router.my_signal_interpreter_app, "run")
def test_main(mock_run):
    with patch("source.main.parse_argument", return_value=MockArgs) as mock_parse_arguments:
        with patch("source.main.register_all_parsers") as mock_register_parsers:
            with patch("source.main.load_signal_database_file") as mock_load_database:
                main()
                mock_parse_arguments.assert_called_once()
                mock_register_parsers.assert_called_once()
                #  mock_load_database.assert_called_with("json", "file_path.json")
                mock_run.assert_called_once()

@patch("source.main.main")
@patch("source.main.__name__", "__main__")
def test_init(mock_main):
    init()
    mock_main.assert_called_once()
    








