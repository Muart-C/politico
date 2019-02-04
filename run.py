import os
from app import create_app

#setup app environment setting to development
app = create_app(environment=os.environ.get('APP_SETTING', 'development'))

if __name__ == "__main__":
    app.run()