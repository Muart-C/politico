import os
import sys

from app import create_app
from api.database.database import DatabaseSetup

environment=os.getenv('APP_SETTING', 'development')
app = create_app(environment)



@app.cli.command()
def createadmin():
    DatabaseSetup().create_admin_if_does_not_exist()

if __name__ == "__main__":
    app.run()