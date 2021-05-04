import requests as requests
import json
import sys

sys.path.append('/Users/alan/')
from secret import *
import logging

logging.basicConfig(level=logging.INFO, filename="venv/app.log")


def get_device_information(site: str) -> dict:
    """
    Gets all of the is-core devices from NetBox

    :return: result_dictionary
    """
    endpoint = NB_URL + 'devices/'
    params = {
        "limit": 0,
        "site": site,
        "tenant": "is-core",
        "role":
            [
                "core_router",
                "provider_edge_router",
                "hosting_provider_edge_router",
                "access_aggregation_switch",
                "console_server",
                "out_of_band_management",
                "server",
                "data_centre_interconnect",
                "route_reflector"
            ]

    }

    logging.info(f"{endpoint}?{params}")

    response = requests.get(endpoint, params, headers=NB_HEADERS)
    json_devices_data = json.loads(response.content)

    result_dictionary = dict()
    for result in json_devices_data['results']:
        result_dictionary[result['id']] = result

    return result_dictionary


if __name__ == '__main__':
    print(json.dumps(get_device_information("randview"), indent=2))

# logging.debug(stuff)
