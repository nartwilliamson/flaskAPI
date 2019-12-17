from flask import Flask, request, render_template, session, redirect, jsonify
import numpy as np
import pandas as pd

from tiingo import TiingoClient
import quandl

quandlAuthToken = "uUfmVoEksfwWxMA4tQcd"

config = {}

# To reuse the same HTTP Session across API calls (and have better performance), include a session key.
config['session'] = True

# If you don't have your API key as an environment variable,
# pass it in via a configuration dictionary.
config['api_key'] = "a5e87637752491cca8c3a282688dbe81f7243561"

#quandl uUfmVoEksfwWxMA4tQcd
# Initialize
client = TiingoClient(config)

app = Flask(__name__)


df = pd.DataFrame({'A': [0, 1, 2, 3, 4],
                   'B': [5, 6, 7, 8, 9],
                   'C': ['a', 'b', 'c--', 'd', 'e']})

def logChange(dataSeries):
    return np.log(dataSeries).diff()

#QUANDL OIL FUTURES
cl1 = quandl.get("CHRIS/CME_CL1", authtoken=quandlAuthToken)
cl1['Date'] = cl1.index
cl1['Date'] = pd.to_datetime(cl1['Date'])
cl1['logChange'] = np.log(cl1.Settle).diff()

cl1 = cl1.drop(['Volume', 'Change','Previous Day Open Interest','Open', 'High', 'Low', 'Last'], axis=1)


dataCSV = pd.read_csv('heatmap_data3.csv') 

ticker_history = client.get_dataframe(['SPY'],
                                      frequency='daily',
                                      metric_name='adjClose',
                                      startDate='2017-01-01',
                                      endDate='2018-05-31')



@app.route('/', methods=("POST", "GET"))
def html_table():
    return render_template('simple.html',  tables=[df.to_html(classes='data')], titles=df.columns.values)

@app.route("/get-data")
def get_data():
    return ticker_history.to_json(orient='records')

@app.route("/cl1")
def get_cl1():
    return cl1.to_json(orient='records')

@app.route('/ticker/<instrument>')
def getInstrument(instrument):
    return '<h1>{}</h1>'.format(instrument)

    
if __name__ == '__main__':
    app.debug = True
    app.run(host= '0.0.0.0', port="5000")