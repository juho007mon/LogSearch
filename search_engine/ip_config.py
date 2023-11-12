# IP sensitive info

import os
import re
import json
import logging
import subprocess

from typing import Dict
from config import EnvConfig


def remove_extension(filename):
    return os.path.splitext(filename)[0]

class LogInfo:
    def __init__(self, config:Dict[str,str]):
        assert isinstance(config, dict), "LogInfo : Unexpected Type"
        self.regex  = re.compile(config["regex"])
        self.parser = config["parser"]
        self.p_args = config["p_args"]
        self.ouf_bfn = config["ouf_bfn"] # ouf_bfn={out_fntag}.xxxx

    def parse_log(self, in_fn:str, out_dir:str):
        if not os.path.exists(in_fn):
            logging.error(f"{in_fn} (file) not found")
            return
        if not os.path.exists(in_fn):
            logging.error(f"{out_dir} (dir) not found")
            return

        # Parser script is empty, so no need to parse
        if len(self.parser) < 2 :
            return

        if self.regex.search(in_fn):
            # parse log
            out_fntag=remove_extension(os.path.basename(in_fn))
            out_fn = os.path.join(out_dir, self.ouf_bfn.format(out_fntag=out_fntag))
            # parse log
            cmd = ['python',
                self.parser,
                *(self.p_args.split(' ')),
                out_fn,
                in_fn
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
        LogInfo({"regex":r'logfn\S*\.bin', "parser":"", "p_args":"", "ouf_bfn":""}),
        LogInfo({"regex":r'logfn\S*\.xlsx', "parser":"", "p_args":"", "ouf_bfn":""}),
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
