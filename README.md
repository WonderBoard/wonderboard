# wonderboard

Notes:

tested on macOS


For enviroment setup:

Add a .flaskenv file in root

In .flaskenv add:

FLASK_APP=manager.py

FLASK_ENV=development

DATABASE_URL=postgres://user:password@hostname/database_name (this is for the local database)

HEROKU_POSTGRES_DATABASE=(this is heroku database url)



Create an eviroment in root:

python3 -m venv venv

activate enviroment

. venv/bin/activate

deactivate enviroment

deactivate


TODO Notes deployment:
Find way to make automate build file to go into root when building frotend
Push database code. (with a possible login feature as well)
