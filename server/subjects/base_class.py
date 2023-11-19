
from __future__ import annotations  # Not needed in Python 3.10+

import os
import logging
import re
import csv
import json
import subprocess
import io
import tempfile
import shutil


from flask import redirect
from flask import Blueprint, request
from flask.json import jsonify
from flask import current_app as cur_app

from typing import Dict, List, Optional, Sequence, Tuple

shpinfo_blpt = Blueprint('shope_info', __name__)

#---------------------------------------------------------------------#
#                                                                     #
#                        LOCAL GLOBAL FUNCTION                        #
#                                                                     #
#---------------------------------------------------------------------#
from abc import ABC, abstractmethod

# Jxx-> Jyy -> Jzz -> Jyy-> Jmem | JLog

#
# User shouldn't inherit this file clase directly.
class LeafFileBase(ABC):
  def __init__(self, log_fpath:str, meta_info:Dict):
    self.log_fpath = log_fpath
    self.meta_info = meta_info
    pass

  @abstractmethod
  def getEsIndex(self) -> Dict:
    # return Index for ES consumable format
    return {
      'filename': os.path.self.log_fpath,
      'path': os.path.dirname()}

# User use this file
class LogFileBase(ABC):
  def __init__(self, log_fpath:str, leaf_files:List[LeafFileBase] = []) :
    self.log_fpath = log_fpath
    self.leaf_files = leaf_files

  @abstractmethod
  def getEsIndex(self) -> Dict:
    # return Index for ES consumable format
    pass

  @abstractmethod
  def genLeafFiles(log_fn:str) -> List[LeafFileBase] :
    return []

class ADbgLog(LogFileBase):
  def __init__(self, log_fpath):
    super().__init__(log_fpath)

    if os.path.exists(log_fpath):
      logging.error(f"File not found : {log_fpath}")
      return None

  def genLeafFiles(log_fn:str) -> List[LeafFileBase] :
    with open('r', log_fn):
      # phydbg analysis
      pass
    
class ABinLog(LogFileBase):
  def __init__(self, log_fpath):
    super().__init__(log_fpath)

    if os.path.exists(log_fpath):
      logging.error(f"File not found : {log_fpath}")
      return None

  def genLeafFiles(log_fn:str) -> List[LeafFileBase] :
    with open('r', log_fn):
      # phydbg analysis
      pass

class JobBase(ABC):
  @abstractmethod
  def __init__(self):
    self.sub_jobs = []
    pass

  @abstractmethod
  def get_nxt_sub_bjob(self):
    for esj in self.sub_jobs:
      yield esj
  
  @abstractmethod
  def 

  

class MyNode:
  def __init__(self, value: int, left: MyNode = None, right: MyNode = None):
    self.value = value
    self.left = left
    self.right = right

  def set_left(self, left: MyNode):
    self.left = left

  def set_right(self, right: MyNode):
    self.right = right

  def get_left(self) -> MyNode:
    return self.left

  def get_right(self) -> MyNode:
    return self.right


# Each Log : File is given
# Entities : things to be searched : ex: 11A, 11B, 11AC ...., 
#   
#

  
#---------------------------------------------------------------------#
#                                                                     #
#                        PAGE                                         #
#                                                                     #
#---------------------------------------------------------------------#
@shpinfo_blpt.route("/tag_index/usr_info_req", methods=["GET", "POST"])
def handle_shop_info_req():
  logging.debug("handle_shop_info_req()")
  logging.debug(request.headers.keys())