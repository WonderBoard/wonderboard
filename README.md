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

Backend(port 5000): 
flask run

frontend(port 3000):
yarn start or npm start


TODO Notes deployment:
Find way to automate build file to go into root when building for frontend
Push database code. (with a possible login feature as well)
