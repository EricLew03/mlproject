from flask import Flask, request, jsonify
import util

app = Flask(__name__)

@app.route('/get_city_names')
def get_city_names():
    response = jsonify({
        'city': util.get_city_names()
    })
    response.headers.add('Access-control-Allow-Origin', '*')

    return response

@app.route('/get_estimated_priec', methods=['Post'])
def predict_home_price():
    total_sqft = float(request.form['sqft'])


    return response

if __name__ == "__main__":
    print("starting Python Flask Server for Home Price Prediction")
    app.run()