import json
import os

def load_json(name):
    file_name = open (name+'.json', 'r')
    data = json.load(file_name)
    file_name.close()
    return data


def list_jsons():
	jsons = []
	for file in os.listdir():
	    if file.endswith(".json"):
	        jsons.append(file)
	return jsons

def write_json(name, data):
    file_name = open(name +'.json', 'w')
    json.dump(data, file_name)
    file_name.close()
