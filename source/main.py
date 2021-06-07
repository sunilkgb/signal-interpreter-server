from argparse import ArgumentParser
from source import router
from source.router import json_parser
# from source.jason_parser import JsonParser
# json_parser = JsonParser()
#router.my_signal_interpreter_app.run()

def parse_argument():
    parser = ArgumentParser()
    parser.add_argument("--file_path")
    return parser.parse_args()

def main():
    args=parse_argument()
    print(args.file_path)
    json_parser.load_file(args.file_path)
    #json_parser.get_signal_title("36")
    router.my_signal_interpreter_app.run()



if __name__ == "__main__":
    main()