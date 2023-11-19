

import os
import logging
import sqlite3

#from sqlite3 import Error, Connection

class MetaDBCntlr:
    def __init__(self, db_fn:str):
        self.db_fn = os.path.realpath(db_fn)
        self.conn = self.create_connection(self.db_fn)

    def connect(self):
        pass

    def close(self):
        self.conn.close()

    @staticmethod
    def create_connection(db_file:str) -> sqlite3.Connection :
        """ Create a database connection to a SQLite database """
        conn = None
        try:
            conn = sqlite3.connect(db_file)
            return conn
        except sqlite3.Error as e:
            print(e)
        return conn

    def create_table(self, create_table_sql):
        """ Create a table from the create_table_sql statement """
        try:
            cursor = self.conn.cursor()
            cursor.execute(create_table_sql)
        except sqlite3.Error as e:
            logging.error(e)

    def commit_to_db(self, sql_cmd:str, sql_args:tuple):
        try:
            cursor = self.conn.cursor()
            cursor.execute(sql_cmd, sql_args)
            self.conn.commit()
        except sqlite3.Error as e:
            logging.error(e)

    def set_issue_parsed(self, jira_issue_id):
        sql = ''' UPDATE issues
                  SET parsed = 1
                  WHERE jira_issue_id = ?'''
        self.commit_to_db(sql, (jira_issue_id,))

    def set_issues_parsed(self, jira_issue_ids, project_names):
        # Prepare the placeholders for jira_issue_ids and project_names
        placeholders_jira = ', '.join('?' * len(jira_issue_ids))
        placeholders_project = ', '.join('?' * len(project_names))
        # Construct the SQL command
        sql_cmd = f''' UPDATE issues
                       SET parsed = 1
                       WHERE jira_issue_id IN ({placeholders_jira})
                       AND project_name IN ({placeholders_project})'''

        # Combine the values into a single tuple for the execute function
        values = tuple(jira_issue_ids) + tuple(project_names)

        # Execute the query
        self.commit_to_db(sql_cmd, values)
        
