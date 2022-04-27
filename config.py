###
# Grab configuration from yml files
###

import yaml

def get_binance_keys():
    with open("./.keys.yml", 'r') as stream:
        try:
            parsed_yaml=yaml.safe_load(stream)
            return parsed_yaml["binance"]['api_key'],parsed_yaml["binance"]['api_secret']
        except yaml.YAMLError as exc:
            print(exc)

def get_setup_config():
    with open("./setup.yml", 'r') as stream:
        try:
            parsed_yaml=yaml.safe_load(stream)
            return parsed_yaml
        except yaml.YAMLError as exc:
            print(exc)
