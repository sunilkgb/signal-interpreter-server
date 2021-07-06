"""
signal routing is handled in this file
"""

import logging
from flask import Flask, request, jsonify, abort
from source.json_parser import JsonParser
from source.xml_parser import XmlParser
from source.parser_factory import ParserFactory
from source.exceptions import InvalidsignalError
json_parser = JsonParser()
xml_parser = XmlParser()
parser_factory = ParserFactory()
my_signal_interpreter_app = Flask(__name__)


logger  = logging.getLogger(__name__)
# @my_signal_interpreter_app.route("/", methods=["GET"])
# def hello():
#     """
#     just test hello world
#     """

#     return "Hello world!"


@my_signal_interpreter_app.route("/", methods=["POST"])
def interpret_signal():
    """
    imterpret a signal
    """
    data = request.get_json()
    try:
        # signal_title = json_parser.get_signal_title(data["signal"])
        signal_title = parser_factory.get_parser().get_signal_title(data["signal"])
        return jsonify(signal_title)
    except KeyError as  err:
        logger.exception(err)
        abort(400, description=f"{data} is not in valid format,except the key to be 'signal'.")
    except InvalidsignalError as err:
        logger.exception(err)
        abort(404, discription=f"there is no {data['signal']} avialable ")

    # return str(data["signal"])
# my_signal_interpreter_app.run()
