
import os
import jira
import dotenv
import urllib3
import getpass
import logging
import pandas as pd

from typing import Any, Dict, Iterable, List, Mapping, Optional, Tuple
from collections import OrderedDict
from jira import Issue, JIRA, JIRAError

from search_engine.config import EnvConfig
from search_engine.models.jira_info import JiraInfo

MAX_SEARCH_RESULT = 1000

class JiraException(Exception):
  """To be raised when a error with the JIRA client occurs."""
  pass

class JiraClient:

  @classmethod
  def from_login(cls,
      jira_url:str=EnvConfig.JIRA_URL,
      cert_fn:str=EnvConfig.JIRA_CERT_FN,
      fldns_to_srch = EnvConfig.JiraCSV_E.LOG_KEYS,
    ) :
    cur_usr = input("Username: ")
    cur_pwd = getpass.getpass("Password: ")
    return cls(jira_url,  cert_fn, cur_usr, cur_pwd, fldns_to_srch)

  @classmethod
  def from_token(cls,
      token_id:str,
      jira_url:str=EnvConfig.JIRA_URL,
      cert_fn:str=EnvConfig.JIRA_CERT_FN,
      fldns_to_srch = EnvConfig.JiraCSV_E.LOG_KEYS,
    ) :
    return cls(jira_url,  cert_fn, None, None, token_id, fldns_to_srch)

  # @param : various
  def __init__(self, jira_url:str, cert_fn:str, cur_usr:str, cur_pwd:str, api_token:str=None, fldns_to_srch:List[str]=[]) :
    assert os.path.exists(cert_fn) , f"{cert_fn} not found."
    cert_fn = os.path.realpath(cert_fn)
    options = {
      'server': jira_url,
      'verify': cert_fn,
    }
    
    ## Access JIRA
    try:
      if cur_pwd is not None:
        logging.info(f"{jira_url} : {cert_fn} via login {cur_usr}")
        self.jira_hdlr = JIRA(options, basic_auth=(cur_usr, cur_pwd), logging=True)
      elif api_token is not None:
        logging.info(f"{jira_url} : {cert_fn} via API {api_token}")
        self.jira_hdlr = JIRA(options, token_auth=api_token, logging=True)
    except JIRAError as e:
      error_message = (
        "Error when creating JIRA instance"
      )
      raise JiraException(error_message) from e
  
    self.field_map = self.jira_hdlr.fields()
    self.fldns_to_srch = fldns_to_srch # EnvConfig.JiraCSV_E.LOG_KEYS
    self.fldn2cid = self.get_fld_name_to_fld_id_map( self.jira_hdlr.fields(), fldns_to_srch )
  
  @staticmethod
  def get_fld_name_to_fld_id_map(jira_field_infos:List[Dict], fld_names:List) -> Dict:
    ret_dict = OrderedDict()
    for fld_info in jira_field_infos:
      if fld_info['name'] in fld_names :
        ret_dict[fld_info['name']] =  fld_info['id']
    return ret_dict
  
  # @param : JIRA query
  def search_issues(self, jquery:str, max_srch_res=MAX_SEARCH_RESULT ):
    return self.jira_hdlr.search_issues(jquery, maxResults=max_srch_res)
        
  # @param : fldns_to_srch: List of field name to search 
  # @param : srch_jira_res: Output of 'search_issues' 
  # @return : Dictionary of key and the values of fields.
  def get_flds_from_srch_res(self, fldns_to_srch:List[str], srch_jira_res ) :
    # Need to find Column ID (hash key) for each field to extract
    fld_cid_missed = False
    for fldn in fldns_to_srch:
      if not fldn in self.fldn2cid:
        logging.warning(f"Cannot find Column ID for given Field Name : {fldn}")
        self.fldn2cid = self.get_fld_name_to_fld_id_map( self.jira_hdlr.fields(), fldns_to_srch )
        break

    # Iterate JIRA
    for ejira in srch_jira_res:
      assert isinstance(ejira.key,str), f"Unexpected JIRA Key : {ejira.key}"
      out_entry = {'key': ejira.key}
      for fld_name in fldns_to_srch:
        fld_cid = self.fldn2cid[fld_name]
        fld_val = ejira.fields.__dict__.get(fld_cid)
        out_entry[fld_name] = fld_val
      yield out_entry

  # @brief : yield dicionary for each JIRA , key is key and field names
  # @param : query: Jira Query 
  # @param : field_names: List of field name to search 
  def gen_srch_entries(self, jquery, field_names, max_num_srch=100):
    srch_res = self.search_issues(jquery, max_num_srch)
    jira_entries =  self.get_flds_from_srch_res(field_names, srch_res)
    return jira_entries

