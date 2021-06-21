import pytest
from unittest.mock import patch
from source.main import parse_argument, ArgumentParser,main, init
from source import router
from source.json_parser import JsonParser


class MockArgs:
    file_path = "path/to/file"

@patch.object(ArgumentParser,"add_argument")
@patch.object(ArgumentParser,"parse_args",return_value=MockArgs)
def test_parse_argument(mock_parse_args,mock_add_argument):
     assert parse_argument() == MockArgs
     mock_parse_args.assert_called_once()
     mock_add_argument.assert_called_with("--file_path")

@patch("source.main.parse_argument", return_value=MockArgs)
@patch.object(JsonParser, "load_file")
@patch.object(router.my_signal_interpreter_app, "run")
def test_main(mock_signal_interpreter_app_run, mock_load_file, mock_parse_args):
    main()
    mock_parse_args.assert_called_once()
    mock_load_file.assert_called_with(MockArgs.file_path)
    mock_signal_interpreter_app_run.assert_called_once()


@patch("source.main.main")
@patch("source.main.__name__", "__main__")
def test_init(mock_main):
    init()
    mock_main.assert_called_once()
    








