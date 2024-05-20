from flask_script import Manager
from flask_migrate import MigrateCommand
from app import app
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy(app)
manager = Manager(app)
manager.add_command("db", MigrateCommand)

if __name__ == "__main__":
    manager.run()
