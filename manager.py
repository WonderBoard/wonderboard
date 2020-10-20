import time
import os
import requests
import psycopg2
from flask_cors import CORS
from flask_session import Session
from flask import Flask, session, redirect, render_template, request, jsonify, flash, json
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from werkzeug.security import check_password_hash, generate_password_hash

#DATABASE_URL=postgres://postgres:Sugarnax93@localhost:5432/wonderboard

app = Flask('__name__', static_folder="./build", static_url_path='/')

# url = urlparse.urlparse(os.environ['DATABASE_URL'])
# db = "dbname=%s user=%s password=%s host=%s " % (url.path[1:], url.username, url.password, url.hostname)
# # schema = "schema.sql"
# conn = psycopg2.connect(db)
# cur = conn.cursor()

#connection with local server, psycopg2 way
# con = psycopg2.connect(
#     host= os.getenv("HOSTS"),
#     database = os.getenv("DATABASES"),
#     user = os.getenv("USERS"),
#     password = os.getenv("PASSWORDS")
# )

# con = psycopg2.connect(
#     host= os.getenv("HOST"),
#     database = os.getenv("DATABASE"),
#     user = os.getenv("USER"),
#     password = os.getenv("PASSWORD")
# )

# Check for environment variable
# HEROKU_POSTGRES_DATABASE
if not os.getenv("DATABASE_URL"):
    raise RuntimeError("DATABASE_URL is not set")


# heroku and local database go here: for local postgres://user:password@hostname/database_name'
engine = create_engine(os.getenv('DATABASE_URL'))

# Configure session to use filesystem
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)
CORS(app)

# Set up database

# create a 'scoped session' that ensures different users' interactions with the
# database are kept separate
db = scoped_session(sessionmaker(bind=engine))

@app.route('/')
def index():
    return app.send_static_file('index.html')

@app.route('/api/time')
def get_current_time():
    row = db.execute("Select * from users")
    
    bookId = row.fetchone()
    print(bookId)
    # resut = conn.execute('Select * from users')
    # cursor
    # cur = con.cursor()
    # cur.execute('Select * from users')
    # rows = cur.fetchall()
    # for r in rows:
    #     print(f"name {r[0]} did {r[1]}")

    # # #close the connection
    # con.close()

    return {'time': time.time()}




@app.route("/api/register", methods=["POST", "GET"])
def register():
    
    json_response = request.json

    return json_response
    # Forget any user_id
    # session.clear()
    
    # User reached route via POST (as by submitting a form via POST)
    # @app.route("/register", methods=["GET", "POST"])
    # def register():

    #Convert json request to dict
    # json_response = request.json
    """ Register user """
    # print("hello")
    # '''
    # Testing things
    # '''
    # print(request.data)
    # x =  '{ "name":"John", "age":30, "city":"New York"}'
    # grabbing data and converting to Dict
    # turns json into dict
    # x = json.loads(x)
    # y = json.loads(json_response)
    # print(x)
    # if request.method == "POST":
        # Ensure username was submitted
        # print("hello")
        # if not request.form.get("username"):
        #     return render_template("error.html", message="must provide username")
    # if request.method == "GET":
    #     print("Get request")
    
    # json_response = request.json

    # grabbing value
    # print(json_response['name'])


@app.route("/api/login", methods=["POST", "GET"])
def login():
    
    json_response = request.json

    return json_response


@app.route("/api/logout", methods=["POST", "GET"])
def logout():
    
    json_response = request.json

    return json_response