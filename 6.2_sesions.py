from flask import Flask, session

app = Flask(__name__)
app.secret_key = '\xb0B=\x10]d\xd7H\x07\x8e~wW\xa7s\xdd\x1b\xeb\x14\xf6W\xa1\xb3\x1f'

@app.route('/')
def index():
  return "Root route for the seesions example"
 
@app.route('/session/write/<name>/')
def write(name=None):
  session['name'] = name
  return "Wrote %s into 'name' key of session" % name

@app.route('/session/read/')
def read():
  try:
    if(session['name']):
      return str(session['name'])
  except KeyError:
      pass
  return "No session variable set for 'name' key"

@app.route('/session/remove/')
def remove():
  session.pop('name', None)
  return "Removed key 'name' from session"

if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
