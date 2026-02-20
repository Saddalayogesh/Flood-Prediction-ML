from flask import Flask, render_template, request
from joblib import load
import numpy as np

app = Flask(__name__)

# Load model and scaler
model = load("floods.save")
sc = load("transform.save")


# Home page
@app.route('/')
def home():
    return render_template("home.html")


# Prediction page
@app.route('/index')
def index():
    return render_template("index.html")


# Prediction logic
@app.route('/data_predict', methods=['POST'])
def predict():
    try:
        temp = float(request.form['temp'])
        humidity = float(request.form['humidity'])
        cloud = float(request.form['cloud'])
        annual = float(request.form['annual'])
        janfeb = float(request.form['janfeb'])
        marmay = float(request.form['marmay'])
        junsep = float(request.form['junsep'])
        octdec = float(request.form['octdec'])
        avgjune = float(request.form['avgjune'])
        sub = float(request.form['sub'])

        data = [[temp, humidity, cloud, annual,
                 janfeb, marmay, junsep,
                 octdec, avgjune, sub]]

        scaled_data = sc.transform(data)
        prediction = model.predict(scaled_data)

        if prediction[0] == 1:
            return render_template("chance.html",
                                   result="⚠ High Possibility of Flood")
        else:
            return render_template("nochance.html",
                                   result="✅ No Flood Risk")

    except Exception as e:
        return str(e)


if __name__ == "__main__":
    app.run(debug=True)
