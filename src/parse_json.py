import json
from os import path

path_name = path.join(path.dirname(__file__), '../data/probabilities.json')

json_file = open(path_name, 'r')
json_obj = json.load(json_file)


print(json_obj["probabilities"][0])
