import pytest
from unittest.mock import patch
from source.main import parse_argument, ArgumentParser


class MockArgs:
    file_path = "path/to/file"

@patch.object(ArgumentParser,"add_argument")
@patch.object(ArgumentParser,"parse_args",return_value=MockArgs)
def test_parse_argument(mock_parse_args,mock_add_argument):
     assert parse_argument() == MockArgs
     mock_parse_args.assert_called_once()
     mock_add_argument.assert_called_with("--file_path")
     
     
# TODO: Missing test main function
