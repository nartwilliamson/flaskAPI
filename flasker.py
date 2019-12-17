# serve.py

#https://stackabuse.com/serving-static-files-with-flask/

from flask import Flask
from flask import render_template

# creates a Flask application, named app
app = Flask(__name__)
app.run(debug=True)

# a route where we will display a welcome message via an HTML template
@app.route("/")
def hello():
    message = "working"
    return render_template('index.html', message=message)

# run the application
if __name__ == "__main__":
    app.run(debug=True)

