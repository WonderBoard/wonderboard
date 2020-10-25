from flask import request, session
from functools import wraps
import time

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        # print(session.get('user_id'))
        if session.get('user_id') == None:
            print("no user_id")
            return {"error": "login required"}
        return f(*args, **kwargs)
    return decorated_function