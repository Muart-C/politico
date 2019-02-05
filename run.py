import os
import sys

from app import create_app

#setup app environment setting to development
#environment=os.getenv('APP_SETTING', 'development')
app = create_app()

if __name__ == "__main__":
    app.run()