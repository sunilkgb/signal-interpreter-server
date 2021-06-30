"""
json parser logic is covered in this file
"""
import ast
import logging
from source.exceptions import InvalidsignalError, JsonParserError


logger = logging.getLogger(__name__)


class JsonParser:
    """
    class to handle the json parser
    """
    def __init__(self):

        """
        intiate the variables
        """

        self.data = {}

    def load_file(self, file_path):
        """
        load a json file
        """

        try:
            with open(file_path, "r") as my_file:
                self.data = ast.literal_eval(my_file.read())
                logger.info("successfuly loaded %s", file_path)
        except FileNotFoundError as err:
            logger.exception("could not find %s", file_path)
            raise JsonParserError from err




    def get_signal_title(self, identifier):
        """
            get signal title from the file
        """
        try:
            for service in self.data["services"]: # pragma: no branch
                if service["id"] == identifier: # pragma: no branch
                    return service["title"]
        except Exception as err:
            raise InvalidsignalError(f"{identifier} not a valid signal") from err
