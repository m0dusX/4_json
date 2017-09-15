import json
import sys 


def load_data(filepath):
	with open (filepath, 'r', encoding="utf-8") as file:
		return json.load(file)

def pretty_print_json(data_to_print):
    print(json.dumps(data_to_print, indent=4, sort_keys=True, ensure_ascii=False))
       
if __name__ == "__main__":
    pretty_print_json(load_data(sys.argv[1]))
