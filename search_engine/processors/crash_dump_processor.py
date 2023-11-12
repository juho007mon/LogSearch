


import os
import re
import logging
import shutil
import subprocess

from typing import Dict, List
from re import Pattern
from ip_config import IPConfig


def find_matching_files(log_dir:str, logfn_regex:List[Pattern]):
    matched_files = []

    # Walk through the directory
    for dirpath, dirnames, filenames in os.walk(log_dir):
        for file in filenames:
            # base filenames
            # Check if file matches any of the regular expressions
            if any(regex.match(file) for regex in logfn_regex):
                matched_files.append(os.path.join(dirpath, file))

    return matched_files


class CrashDumpProcessor:
    @classmethod
    def from_scratch_dir(cls,scratch_dir):
        return cls(scratch_dir)

    def __init__(self, scratch_dir:str):
        assert os.path.exists(scratch_dir), "scratch_dir not found"
        self.scratch_dir = scratch_dir

    def search_log_files(self, entries:List[Dict]):
        for entry in entries :
            issue_key = entry.get('key')
            log_path =  entry.get('Logs')
            if log_path is None : 
                continue
            if not os.path.exists(log_path):
                continue
            if issue_key is None :
                continue

            log_files = []
            
            # logfn regular expressions
            logfns_regexes = [ loginfo.regex for loginfo in IPConfig.logfn_infos]

            # Iterate possible log paths
            for e_pth in IPConfig.hwlog_subpaths:
                hwlog_path = os.path.join(log_path, *e_pth)
                sub_files = find_matching_files(hwlog_path,  logfns_regexes)   
                # Iterate possible logs in each path
                for efn in sub_files:
                    log_files.append(os.path.join(self.scratch_dir,efn))
                    logging.info(f"{issue_key} : {efn}")
            
            if not os.path.exists(self.scratch_dir):    
                logging.error(f"{self.scratch_dir} not found.")
                continue
            
            add_entry = {
                'log_files': log_files,
            }
            entry.update(add_entry)

            yield entry

    def copy_log_files(self, entries:List[Dict]):
        for entry in entries:
            issue_key = entry.get('key')

            # Create Local Path in server
            local_path = os.path.join(self.scratch_dir, issue_key)
            if not os.path.exists(local_path):
                os.mkdir(local_path)
            if not os.path.exists(local_path):
                logging.error(f"Create {local_path} failed")
                assert False

            local_log_files = []
            for e_fn in entry['log_files'] :
                l_fn = os.path.join(local_path, os.path.basename(e_fn))
                shutil.copy(e_fn, l_fn)
                local_log_files.append(l_fn)

            add_entry = {
                "local_path":local_path,
                "local_log_files": local_log_files,
            }
            entry.update(add_entry)

            yield entry

    def parse_log_files(self, entries:List[Dict]):
        for entry in entries:
            local_path = entry["local_path"]
            # issue_key = entry["key"]
            for e_fn in entry['local_log_files'] :
                # Consider move below code to IPConfig
                for e_info in IPConfig.logfn_infos:
                    e_info.parse_log(e_fn, local_path)
                    
            yield entry

    def process_dump(self, dump_location):
        # process the crash dump
        # extract necessary information
        # possibly using your generator function
        pass