import os
import sys

from app import create_app
from api.database.database import DatabaseSetup
#setup app environment setting to development
environment=os.getenv('APP_SETTING', 'development')
app = create_app(environment)


@app.cli.command()
def create():
    DatabaseSetup().create_tables()

@app.cli.command()
def delete():
    DatabaseSetup().drop_data_from_tables()

if __name__ == "__main__":
    app.run(port=5001)