# IP sensitive info

import os
import re
import json
import logging
import subprocess

from typing import Dict, List
from config import EnvConfig


def remove_extension(filename):
    return os.path.splitext(filename)[0]

class LogInfo:
    def __init__(self, config:Dict[str,str|List]):
        assert isinstance(config, dict), "LogInfo : Unexpected Type"
        self.regex  = re.compile(config["regex"])
        self.parser_cmd_args = config["parser_cmd_args"]

    def parse_log(self, in_fn:str, out_dir:str):
        if not os.path.exists(in_fn):
            logging.error(f"{in_fn} (file) not found")
            return
        if not os.path.exists(in_fn):
            logging.error(f"{out_dir} (dir) not found")
            return

        # Parser script is empty, so no need to parse
        if len(self.parser_cmd_args) < 1 :
            return

        if self.regex.search(in_fn):
            # parse log
            out_fntag = remove_extension(os.path.basename(in_fn))
            cmd = [
                carg.format(out_fntag=out_fntag,input_fn=in_fn) for carg in self.parser_cmd_args
            ]
            try:
                logging.info(f"Script : {' '.join(cmd)}")
                proc = subprocess.Popen(cmd, universal_newlines=True)
                proc.wait()
                stdout, stderr = proc.communicate()
                if proc.returncode != 0:
                    logging.error(f"Script Error: {stderr}")
                else:
                    logging.info(f"Script Output: {stdout}")

            except subprocess.CalledProcessError as ex:
                logging.error('"{cmd}" returned code {rc}'.format(cmd=' '.join(cmd), rc=ex.returncode))
            
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
        LogInfo({"regex":"logfn\\S*\\.xlsx", "parser_cmd_args":["echo","test", "{input_fn}"], "args_var":["input_fn"]}),
        LogInfo({"regex":"binfn\\S*\\.bin", "parser_cmd_args":["echo","test", "{input_fn}"], "args_var":["input_fn"]}),
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
