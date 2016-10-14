#import Flask and Bootstrap classes
from flask import Flask, redirect, url_for, abort, request
from flask_bootstrap import Bootstrap

def create_app():
  app = Flask(__name__)
  Bootstrap(app)

  return app

@app.route('/')
def index():
  return 'This is the home page'

if __name__ == '__main__':
  app.run(debug=True)
