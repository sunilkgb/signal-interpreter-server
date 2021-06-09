import ast
class JsonParser:
    def __init__(self):
        self.data = {}

    def load_file(self, file_path):
        with open(file_path, "r") as my_file:
            self.data = ast.literal_eval(my_file.read())

        
    def get_signal_title(self, identifier):
        data=self.data
        for i in range (len(data["services"])):
            if data["services"][i]["id"] == identifier:
                print(data["services"][i]["title"])
                return data["services"][i]["title"]
