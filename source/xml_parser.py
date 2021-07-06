"""
xml parser logic is covered in this file
"""

import logging
import xml.etree.ElementTree as ET
import xmltodict
from source.exceptions import InvalidsignalError, SignalInterpreterServerException

logger = logging.getLogger(__name__)

class XmlParser:
    """
    class to handle the xml parser
    """
    def __init__(self):

        """
        intiate the variables
        """

        self.data = {}


    def load_file(self, file_path):
        """
        load a xml  file
        """

        try:
            tree = ET.parse(file_path)
            data = tree.getroot()
            xml_string = ET.tostring(data, encoding="utf-8", method="xml")
            self.data = dict(xmltodict.parse(xml_string))
            logger.info(self.data)
        except FileNotFoundError as err:
            logger.exception("could not find %s", file_path)
            raise SignalInterpreterServerException from err


    def get_signal_title(self, identifier):
        """
            get signal title from the file
        """
        try:
            for services in self.data["services"].values(): # pragma: no branch
                for service in services:
                    if service["@id"] == identifier: # pragma: no branch
                        return service["title"]
        except Exception as err:
            raise InvalidsignalError(f"{identifier} not a valid signal") from err
