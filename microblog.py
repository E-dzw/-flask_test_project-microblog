import imp
from re import U
from sqlite3 import dbapi2
from app import app, db
from app.models import User, Post
@app.shell_context_processor
def make_shell_test():
    return {'db': db ,'user': User,'post': Post}