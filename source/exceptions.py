""" Custom Exceptions """

class InvalidsignalError(Exception):
    """ signal not found error """


class JsonParserError(Exception):
    """ Unable to parse the json file """

class SignalInterpreterServerException(Exception):
    """ Signal Interpreter Server Exception"""
