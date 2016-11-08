from flask import Flask, g
import sqlite3

app = Flask(__name__)
# remember to add var dir to your CW app for holding db
db_location = 'var/test.db'

def get_db():
  db = gettattr(g, 'db', None)
  if db is None:
    db = sqlite3.connect(db_location)
    g.db = db
  return  db


