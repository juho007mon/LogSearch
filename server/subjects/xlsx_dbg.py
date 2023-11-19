
import os
import logging
import openpyxl as pxl
from .base_class import LogFileBase


class XLDbgLog(LogFileBase):
  def __init__(self, log_fpath):
    super().__init__(log_fpath)
    if os.path.exists(log_fpath):
      logging.error(f"File not found : {log_fpath}")

    self.entities = []

  def genLeafFiles(log_fn:str) :
    return []

  def parseLog():
    # Search and get Entity

