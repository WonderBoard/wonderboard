import time
import os
import requests
import psycopg2
from decorator import login_required
from flask_cors import CORS
from flask_session import Session
from flask import Flask, session, request, jsonify, flash, json
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from werkzeug.security import check_password_hash, generate_password_hash

app = Flask('__name__', static_folder="./build", static_url_path='/')
app.secret_key = "abc"  

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

# session file system
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)
CORS(app)

# make sure each user has own session
db = scoped_session(sessionmaker(bind=engine))

@app.route('/')
def index():
    return app.send_static_file('index.html')

@app.route('/api/time', methods=["POST", "GET"])
@login_required
def get_current_time():
    row = db.execute("Select * from users")
    
    testrow = row.fetchone()
    print(testrow)
    # resut = conn.execute('Select * from users')
    # cursor
    # cur = con.cursor()
    # cur.execute('Select * from users')
    # rows = cur.fetchall()
    # for r in rows:
    #     print(f"name {r[0]} did {r[1]}")

    # # #close the connection
    # con.close()

    return {'times': time.time()}




@app.route("/api/register", methods=["POST", "GET"])
def register():
    
    #{
    #"username": "hae2222",
    #"email": "email@emaild2dd323w363.com",
    #"password": "daosdkd",
    #"confirmation": "hl"
    # }
    
    session.clear()
    
    json_response = request.json

    print(json_response.get("username"))

    # email = json_response.get("email")

    # print(" {}  this is get".format(json_response.get('username')))
    # username = json_response.get("username")

    # if 

    # print(username)

    # print(json_response)
    if request.method == "POST":

        # username not empty
        if json_response.get("username") == '':
            return {"message": "no username", "success": False}

        # password not empty
        elif json_response.get("password") == '':
            return {"message": "no password", "success": False}
        
        # email not empty
        elif json_response.get("email") == '':
            return {"message": "no email", "success": False}
        
        # confirmation not empty
        elif json_response.get("confirmation") == '':
            return {"message": "no confirmation", "success": False}

        # query to see if email exist in database
        email_check = db.execute("SELECT * FROM users WHERE user_email = :email",
                        {"email": json_response.get("email")}).fetchone()
        
        # check if email already exists
        if email_check:
            return {"message": "email exists", "success": False}
        
        print(email_check)

        # hash password
        hash_pass = generate_password_hash(json_response["password"], method='pbkdf2:sha256', salt_length=8)


        # Insert register info
        db.execute("INSERT INTO users (user_name, user_email, user_password) VALUES (:username, :useremail, :password)",
                            {"username":json_response.get("username"),
                            "useremail":json_response.get("email"),
                             "password":hash_pass})

        db.commit()

    return { "message" : "congrats for registering", "success": True}



    # Forget any user_id
    # session.clear()
    
    # User reached route via POST (as by submitting a form via POST)
    # @app.route("/register", methods=["GET", "POST"])
    # def register():

    #Convert json request to dict
    # json_response = request.json


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

    print(json_response)
    
    # session.clear()

    # for request
    email = json_response.get("email")
    
    
    if request.method == "POST":

        # check if username was submitted
        if json_response.get("email") == "":
            return {"messgage": "no email", "success": False}

        # check if password was submitted
        elif json_response.get("password") == "":
            return {"messgage": "no password", "success": False}

        # select were unique email is
        rows = db.execute("SELECT * FROM users WHERE user_email = :email",
                            {"email": email})
        
        #extract row
        row_result = rows.fetchone()

        #get hashed password 
        hashed_pass = row_result[3]

        # print(result)
        # verify result and hashed password
        if  row_result == None or not check_password_hash(hashed_pass, json_response["password"]):
            return {"error": "username exists and password is correct"}

        # Get info from user and store it
        session['userid'] = "hello"
        session['username'] = row_result[1]
        session['useremail'] = row_result[2]

        print(session.get('user_id'))
        # home page
        return {"redirect": "homepage"}

    # login
    else:
        return {"redirect": "login"}

    return json_response


@app.route("/api/logout", methods=["POST", "GET"])
def logout():
    session.clear()
    json_response = request.json

    return {"message": "logout"}

@app.route("/api/checksession", methods=["POST", "GET"])
# @login_required
def checking():
    # print('hello')
    if session.get('userid') == None:
          print("hello") 
    json_response = request.json
    # print(session.get("user_id"))
    # return  session["user_id"
    return json_response