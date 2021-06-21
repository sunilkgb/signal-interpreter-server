"""
signal routing is handled in this file
"""

from flask import Flask, request, jsonify
from source.json_parser import JsonParser
json_parser = JsonParser()
my_signal_interpreter_app = Flask(__name__)


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
    signal_title = json_parser.get_signal_title(data["signal"])
    return jsonify(signal_title)
    # return str(data["signal"])
# my_signal_interpreter_app.run()
