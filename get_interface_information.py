import json
import sys

import requests

sys.path.append('/Users/alan/')
from secret import *
import logging

logging.basicConfig(level=logging.INFO, filename="app.log")


def main(site: str) -> dict:
    """
    Gets all of the is-core interfaces from NetBox

    :return: result_dictionary
    """
    endpoint = NB_URL + 'interfaces/'
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


if __name__ == '__main__':
    main()

# logging.debug(stuff)
