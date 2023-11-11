# IP sensitive info

import os
import json

from config import EnvConfig

class IPConfig:
    version = 0.1
    test_jquery = 'project = MYPROJECT'

    # possible subpaths
    hwlog_subpaths = [
        ['MY_Logs','CUST_HW']
    ]
    # possible filename pattern
    logfns_regex = [
        r'logfn\S*\.bin',
        r'logfn\S*\.xlsx',
    ]

    class someTypeE:
        car = 0
        plane = 1

    @classmethod
    def update_from_json(cls, json_file):
        with open(json_file, 'r') as file:
            data = json.load(file)
            for key, value in data.items():
                if hasattr(cls, key):
                    setattr(cls, key, value)
                elif hasattr(cls.someTypeE, key):
                    setattr(cls.someTypeE, key, value)

if os.path.exists(EnvConfig.IP_CONFIG_JSON) :
    IPConfig.update_from_json(EnvConfig.IP_CONFIG_JSON)
