# wonderboard

Notes:
tested on macOS

For enviroment setup:

Add a .flaskenv file in root

In the .flaskenv

FLASK_APP=manager.py

FLASK_ENV=development

DATABASE_URL=postgres://user:password@hostname/database_name (this is for the local database)

HEROKU_POSTGRES_DATABASE=(this is heroku database url)

Create an eviroment in root

python3 -m venv venv

activate enviroment

. venv/bin/activate

deactivate enviroment

deactivate


