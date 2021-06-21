"""
main function of the program
"""

from argparse import ArgumentParser
from source import router
from source.router import json_parser
# from source.jason_parser import JsonParser
# json_parser = JsonParser()
# router.my_signal_interpreter_app.run()


def parse_argument():
    """
    basic argument parser
    """

    parser = ArgumentParser()
    parser.add_argument("--file_path")
    return parser.parse_args()


def main():
    """
    main function call
    """

    args = parse_argument()
    print(args.file_path)
    json_parser.load_file(args.file_path)
    # json_parser.get_signal_title("36")
    router.my_signal_interpreter_app.run()


def init():
    """
    hack of all hacks, to get the 100 percent code coverage :)
    """

    if __name__ == "__main__":
        main()

init()
