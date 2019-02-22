import os
import sys

from app import create_app
from api.database.database import DatabaseSetup

environment=os.getenv('APP_SETTING', 'development')
app = create_app(environment)
if __name__ == "__main__":
    python api_docs.py
    app.run()
