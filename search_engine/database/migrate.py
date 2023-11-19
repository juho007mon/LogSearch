# Offline Script doing SQL DB migration

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from web_app import app, db  
from models.sql_db_models import JiraIssue

# Initialize Flask-Migrate
migrate = Migrate(app, db)

if __name__ == '__main__':
    # Run the migration commands
    with app.app_context():
        migrate.init_app(app, db)
        migrate.create()
        migrate.migrate()
        migrate.upgrade()
