from flask import Flask, render_template, url_for, request
import pandas as pd
import numpy as np
import pickle

# load the model from disk
filename = 'modelExtra.pkl'
model = pickle.load(open(filename, 'rb'))

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        me = request.form['message']
        message = [float(x) for x in me.split(',')]
        vect = np.array(message).reshape(1, -1)
        my_prediction = model.predict(vect)
    return render_template('result.html', prediction=my_prediction)


if __name__ == '__main__':
    app.run(debug=True)
