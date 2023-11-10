# IP sensitive info

import os
import json

IPCONFIG_JSON_FN = 'ip_config.json'

class IPConfig:
    version = 0.1
    test_jquery = 'project = MYPROJECT'

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

if os.path.exists(IPCONFIG_JSON_FN) :
  IPConfig.update_from_json(IPCONFIG_JSON_FN)
