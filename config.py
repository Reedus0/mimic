import json

from logger import *

def read_config():
    log("Reading config...")
    with open ("config.json", "r") as file:
        file_data = file.read()
        return json.loads(file_data)
    
def write_config(data):
    log("Writing config...")
    with open ("config.json", "w") as file:
        file_data = json.dumps(data)
        file.write(file_data)