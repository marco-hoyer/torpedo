from torpedo import instance_metadata
import yaml


def _parse_yaml_userdata():
    """
    Read user-data string and parse it as yaml
    :return: dict
    """
    user_data_string = instance_metadata.user_data()
    return yaml.safe_load(user_data_string)


def get_config():
    """
    Get torpedo configuration
    :return: dict
    """
    return _parse_yaml_userdata()
