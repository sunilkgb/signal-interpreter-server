from argparse import ArgumentParser
from source import router
from source.router import json_parser

def parse_argument():
    parser = ArgumentParser()
    parser.add_argument("--file_path")
    return parser.parse_args()

def main():
    args=parse_argument()
    json_parser.load_file(args.file_path)
    router.my_signal_interpreter_app.run()



if __name__ == "__main__":
    main()