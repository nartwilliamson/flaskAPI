from flask import Flask
from flask import render_template
app = Flask(__name__)


@app.route('/')
def hello():
    message = "glance.ai"
    return render_template('index.html', message=message)
    
if __name__ == '__main__':
    app.debug = True
    app.run(host= '0.0.0.0', port="5000")