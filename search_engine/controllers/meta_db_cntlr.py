
import os
import sqlite3
from sqlite3 import Error, Connection


class MetaDBCntlr:
    def __init__(self, db_fn:str):
        self.db_fn = os.path.realpath(db_fn)
        self.conn = self.create_connection(self.db_fn)

    @staticmethod
    def create_connection(db_file:str) -> Connection :
        """ Create a database connection to a SQLite database """
        conn = None
        try:
            conn = sqlite3.connect(db_file)
            return conn
        except Error as e:
            print(e)
        return conn

    def create_table(conn:Connection, create_table_sql):
        """ Create a table from the create_table_sql statement """
        try:
            c = conn.cursor()
            c.execute(create_table_sql)
        except Error as e:
            print(e)

    def update_issue(self, jira_issue_id):
        sql = ''' UPDATE issues
                  SET parsed = 1
                  WHERE jira_issue_id = ?'''
        cur = self.conn.cursor()
        cur.execute(sql, (jira_issue_id,))
        self.conn.commit()

    def update_issues(self, jira_issue_ids, project_names):
        # Prepare the placeholders for jira_issue_ids and project_names
        placeholders_jira = ', '.join('?' * len(jira_issue_ids))
        placeholders_project = ', '.join('?' * len(project_names))

        # Construct the SQL command
        sql = f''' UPDATE issues
                SET parsed = 1
                WHERE jira_issue_id IN ({placeholders_jira})
                AND project_name IN ({placeholders_project})'''

        # Combine the values into a single tuple for the execute function
        values = tuple(jira_issue_ids) + tuple(project_names)

        # Execute the query
        cur = self.conn.cursor()
        cur.execute(sql, values)
        self.conn.commit()