
import os
import argparse

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Config
from ip_config import IPConfig
from config import EnvConfig

# Sub page
from blueprints.search import search_bp
from blueprints.issue_tracker import issue_tracker_bp

# Modules
from controllers.issue_tracker_controller import IssueTrackerController
from utils.logger import cfg_dbg_logger

#---------------------------------------------------------------------#
#          APP                                                        #
#---------------------------------------------------------------------#
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{EnvConfig.SQL_DB_FILE}'
app.register_blueprint(search_bp)
app.register_blueprint(issue_tracker_bp)

#---------------------------------------------------------------------#
#          DB (SQL)                                                   #
#---------------------------------------------------------------------#
db = SQLAlchemy()
db.init_app(app)
with app.app_context():
    db.create_all()

#---------------------------------------------------------------------#
#          BASE                                                       #
#---------------------------------------------------------------------#
@app.route("/")
def hello_world():
    return "<p>This is backend server, please get/post to proper URL.</p>"


#---------------------------------------------------------------------#
#     MAIN                                                            #
#---------------------------------------------------------------------#
def main():
    '''Entry point'''
    parser = argparse.ArgumentParser(description='WebApp')
    grp_misc = parser.add_argument_group('Misc', 'Miscellaneous analysis modes and output flags')
    grp_misc.add_argument('--debug', default=False, action='store_true', help='Enable debug log')
    args = parser.parse_args()

    cfg_dbg_logger(app, args.debug)

    app.run(host=EnvConfig.IP, port=EnvConfig.PORT, debug=args.debug)
  
if __name__ == "__main__":
    main() 
