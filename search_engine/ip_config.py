# IP sensitive info

import os
import re
import json
import logging
import subprocess
from typing import Dict, List

from search_engine.config import EnvConfig
from search_engine.models.log_info import LogInfo

class IPConfig:
    version = 0.1
    test_jquery = 'project = MYPROJECT'
    srch_jquery = 'project = MYPROJECT'

    # possible subpaths
    hwlog_subpaths = [
        ['path_lvl0','path_lvl1','path_lvl2']
    ]

    # possible filename pattern
    logfn_infos = [
        LogInfo.from_dict({"regex":"logfn\\S*\\.xlsx", "parser_cmd_args":["echo","test", "{input_fn}"], "args_var":["input_fn"]}),
        LogInfo.from_dict({"regex":"binfn\\S*\\.bin", "parser_cmd_args":["echo","test", "{input_fn}"], "args_var":["input_fn"]}),
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
                    if key == "logfn_infos":
                        value = [LogInfo(vd) for vd in value]
                    setattr(cls, key, value)
                elif hasattr(cls.someTypeE, key):
                    setattr(cls.someTypeE, key, value)

if os.path.exists(EnvConfig.IP_CONFIG_JSON) :
    IPConfig.update_from_json(EnvConfig.IP_CONFIG_JSON)
