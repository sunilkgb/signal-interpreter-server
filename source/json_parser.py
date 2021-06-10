import ast
# Why not use the json library instead

class JsonParser:
    def __init__(self):
        self.data = {}

    def load_file(self, file_path):
        with open(file_path, "r") as my_file:
            self.data = ast.literal_eval(my_file.read())
            # with the json library we can instead use 
            # self.data = json.load(my_file)

        
    def get_signal_title(self, identifier):
        data=self.data
        # no need to make a copy of self.data, we only want to look at it
        # not modify it
        for i in range (len(data["services"])):
            if data["services"][i]["id"] == identifier:
                print(data["services"][i]["title"])
                return data["services"][i]["title"]
