"""
  python -m unittest  tests.test_jira_client
"""

import unittest
import logging

#from ..config import EnvConfig
#from ..ip_config import IPConfig
from search_engine.config import EnvConfig
from search_engine.ip_config import IPConfig
from search_engine.clients.jira_client import JiraClient
from search_engine.utils.logger import config_logging

class TestJiraClient(unittest.TestCase):
    def setUp(self):
        # Setup mock Elasticsearch cluster connection here
        config_logging(logging.DEBUG)
        logging.info("START : setUp")

    def test_jira_query(self):
        # Test indexing a document
        jiraServer = JiraClient.from_token(
          EnvConfig.JIRA_TOKEN,
        )

        jquery = IPConfig.test_jquery
        logging.info(jquery)
        jira_entries = jiraServer.gen_srch_entries(jquery, EnvConfig.JiraCSV_E.LOG_KEYS, 20)

        for entry in jira_entries:
          logging.debug(entry)

    def tearDown(self):
        # Test searching documents
        logging.info("DONE : tearDown")

if __name__ == '__main__':
    unittest.main()