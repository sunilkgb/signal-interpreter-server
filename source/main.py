"""
main function of the program
"""

import logging
from argparse import ArgumentParser
from source import router
from source.router import parser_factory
from source.xml_parser import XmlParser
from source.json_parser import JsonParser
# json_parser = JsonParser()
# router.my_signal_interpreter_app.run()

logger = logging.getLogger(__name__)


def parse_argument():
    """
    basic argument parser
    """

    parser = ArgumentParser()
    parser.add_argument("--file_path")
    return parser.parse_args()

def register_all_parsers():
    """
    register all the possible formats
    """

    parser_factory.register_format("xml", XmlParser)
    parser_factory.register_format("json", JsonParser)

def load_signal_database_file(file_format, file_path):
    "load the signal database file"

    parser_factory.set_signal_database_format(file_format)
    selected_parser = parser_factory.get_parser()
    selected_parser.load_file(file_path)


def main():
    """
    main function call
    """

    args = parse_argument()
    print(args.file_path)
    register_all_parsers()
    if args.file_path.endswith("xml"):
        load_signal_database_file("xml", args.file_path)
    elif args.file_path.endswith("json"):
        load_signal_database_file("json", args.file_path)
    logger.info("starting  the signal interpreter app")
    router.my_signal_interpreter_app.run()



def init():
    """
    hack of all hacks, to get the 100 percent code coverage :)
    """

    if __name__ == "__main__":
        main()

init()
