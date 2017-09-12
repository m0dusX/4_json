import json
import sys 


def load_data(filepath):
    file_with_json = open(filepath, "a")
    parsed_json = json.load(file_with_json)
    return parsed_json

def pretty_print_json(data_to_print):
    print(json.dumps(data_to_print, indent=4, sort_keys=True))
       
if __name__ == "__main__":
    pretty_print_json(load_data(sys.argv[1]))
