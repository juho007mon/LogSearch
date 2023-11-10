import os
import logging

from dotenv import load_dotenv
load_dotenv()

# @brief : Load Enviroment Variable
class EnvConfig:
  CERT_PATH = os.getenv('CERT_PATH')
  JIRA_CERT_FN = os.path.join(CERT_PATH,os.getenv('JIRA_CERT_FN'))
  JIRA_URL  = os.getenv('JIRA_URL')
  JIRA_TOKEN = os.getenv('JIRA_TOKEN')

  class JiraCSV_E:
    ISSUE_KEY    = r'Issue key'
    LOG_KEYS = [r'Logs', r'Crash Log location']


# @brief : Common Logging Config function
def config_logging(log_level:int=logging.INFO):
  log_format = '%(message)s'
  # DEBUG is less than INFO
  if log_level < logging.INFO :
    log_level = logging.DEBUG
    log_format = '%(asctime)s %(module)-15s %(levelname)-8s %(message)s'

  log_format = '%(asctime)s %(module)-15s %(levelname)-8s %(message)s'
  logging.basicConfig(format=log_format, level=log_level)

  # TODO
  log_handler = logging.StreamHandler()
  log_handler.setLevel(log_level)
  log_handler.setFormatter(log_format)

  return log_handler
