"""
json parser logic is covered in this file
"""
import ast


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

        with open(file_path, "r") as my_file:
            self.data = ast.literal_eval(my_file.read())



    def get_signal_title(self, identifier):
        """
            get signal title from the file
        """
        for service in self.data["services"]: # pragma: no branch
            if service["id"] == identifier: # pragma: no branch
                return service["title"]
