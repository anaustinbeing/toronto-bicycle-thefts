# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np
from flask import Flask, request, render_template
import pickle

app = Flask(__name__, template_folder='template')
model = pickle.load(open('model.pkl', 'rb'))
transformer = pickle.load(open('pipeline_transform.pkl', 'rb'))


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict():

    input_data = [x for x in request.form.values()]

    df = pd.DataFrame([input_data], columns=['Primary_Offence', 'Occurrence_DayOfWeek', 'Report_DayOfWeek',
                      'Hood_ID', 'Bike_Make', 'Bike_Type', 'Bike_Colour', 'Cost_of_Bike', 'Location_Type', 'Premises_Type'])
    df = transformer.transform(df)
    output = model.predict(df)
    if output == 0:
        output = "STOLEN"
    else:
        output = "RECOVERED"

    return render_template('index.html', prediction_text='Theft Prediction - {}'.format(output))


if __name__ == "__main__":
    app.run(debug=True)
