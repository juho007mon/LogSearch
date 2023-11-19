import os
import logging

# NOTE: Don't include any dependency on this file 
from dotenv import load_dotenv
load_dotenv()

# @brief : Load Enviroment Variable
class EnvConfig:
  CERT_PATH = os.getenv('CERT_PATH')
  JIRA_CERT_FN = os.path.join(CERT_PATH,os.getenv('JIRA_CERT_FN'))
  JIRA_URL  = os.getenv('JIRA_URL')
  JIRA_TOKEN = os.getenv('JIRA_TOKEN')
  IP_CONFIG_JSON = os.getenv('IP_CONFIG_JSON')
  SQL_DB_FILE = os.getenv('SQL_DB_FILE')

  class JiraCSV_E:
    ISSUE_KEY    = r'Issue key'
    LOG_KEYS = [r'Logs', r'Crash Log location']


