import json
import sys


def load_data(filepath):
    with open(filepath, "r") as f:
        return json.load(f)

def pretty_print_json(data):
    print(json.dumps(data, indent=4, sort_keys=True))
       


if __name__ == '__main__':
    pretty_print_json(load_data(sys.argv[1]))
