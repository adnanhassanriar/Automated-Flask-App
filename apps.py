from flask import Flask, render_template, jsonify
import requests
import pandas as pd
import numpy as np

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/data')
def data():
    try:
        r = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json', timeout=5)
        btc_price = r.json()['bpi']['USD']['rate']
    except:
        btc_price = "API not reachable"
    
    data = pd.DataFrame({
        'value': np.random.rand(5)
    })

    return jsonify({
        'bitcoin_price': btc_price,
        'random_data': data['value'].tolist()
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

