import pandas as pd
import numpy as np
from flask import Flask, request, render_template
import pickle

app = Flask(__name__)
model = pickle.load(open('bimodel.pkl', 'rb'))

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/predict",methods=['POST'])
def getPredict():
    if request.method == 'POST':
        brand_no = request.form['brand_no']
        kms_driven = request.form['kms_driven']
        owner = request.form['owner']
        age = request.form['age']
        power = request.form['power']

        print(brand_no,kms_driven,owner,age,power)
        input = pd.DataFrame([[kms_driven,owner,age,power,brand_no]],columns=['kms_driven','owner','age','power','brand'])
        prediction = "{:.1f}".format(model.predict(input)[0])
    
    return render_template('index.html', prediction_text='Price for your bike is : {} ₹'.format(prediction))

if __name__ == "__main__":
    app.run(debug=True)