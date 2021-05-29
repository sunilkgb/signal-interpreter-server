from flask import Flask,request

my_signal_interpreter_app = Flask(__name__)


@my_signal_interpreter_app.route("/", methods=["GET"])
def hello():
    return "Hello world!"

@my_signal_interpreter_app.route("/", methods=["POST"])
def mirror_data():
    data = request.get_json()
    return data


#my_signal_interpreter_app.run()