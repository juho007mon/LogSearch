"""
  python -m unittest  tests.test_jira_log
"""

import unittest
import logging

from config import EnvConfig, config_logging
from ip_config import IPConfig

from clients.jira_client import JiraClient
from processors.crash_dump_processor import CrashDumpProcessor

class TestJiraLogs(unittest.TestCase):
    def setUp(self):
        # Setup mock Elasticsearch cluster connection here
        config_logging(logging.DEBUG)
        logging.info("START : setUp")

    def test_jira_query(self):
        # Jira Server
        jiraServer = JiraClient.from_token(
          EnvConfig.JIRA_TOKEN,
        )
        # Check log parse Dump File
        dumpProcess = CrashDumpProcessor.from_scratch_dir('C:\scratch')

        jquery = IPConfig.search_jquery
        logging.info(jquery)

        jira_entries = jiraServer.gen_srch_entries(jquery, EnvConfig.JiraCSV_E.LOG_KEYS, 100)
        jira_entries = dumpProcess.search_log_files(jira_entries) 
        jira_entries = dumpProcess.parse_log_files(jira_entries)

        for entry in jira_entries:
            continue
        
    def tearDown(self):
        # Test searching documents
        logging.info("DONE : tearDown")

if __name__ == '__main__':
    unittest.main()