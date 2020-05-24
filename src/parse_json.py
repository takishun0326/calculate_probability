import json
from os import path

path_name = path.join(path.dirname(__file__), '../data/probabilities.json')

json_file = open(path_name, 'r')
json_obj = json.load(json_file)

def get_json():
    json_list = []
    for j in json_obj["probabilities"]:
        json_list.append(str(j["Numerator"]) + "/" + str(j["Denominator"]))
    return json_list

def get_json_value(index):
    return float(json_obj["probabilities"][index]["Numerator"]/json_obj["probabilities"][index]["Denominator"])
