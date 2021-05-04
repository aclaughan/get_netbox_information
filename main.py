import json
import sys

import requests as requests

from get_device_information import *

sys.path.append('/Users/alan/')
from secret import *
import logging

logging.basicConfig(level=logging.INFO, filename="app.log")

if __name__ == '__main__':
    pop_info = dict()
    pop_info["devices"] = get_device_information("randview")

    with open("pop_info.json", "w") as out_file:
        json.dump(pop_info, out_file)
