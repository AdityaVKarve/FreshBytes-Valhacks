from flask import Flask, request, render_template, jsonify
import joblib
import numpy as np
from forms import WineDataForm

app = Flask(__name__)
app.secret_key = "your_secret_key"

# Load the pre-trained model
model = joblib.load("../Model/Pipelines/wine_predictor.joblib")

@app.route('/')
def home():
    wine_dataform = WineDataForm(request.form)
    return render_template('index.html',form=wine_dataform)

@app.route('/predict', methods=['POST'])
def predict():
    # Get form values
    try:
        fixed_acidity = float(request.form['fixed_acidity'])
        volatile_acidity = float(request.form['volatile_acidity'])
        citric_acid = float(request.form['citric_acid'])
        residual_sugar = float(request.form['residual_sugar'])
        chlorides = float(request.form['chlorides'])
        free_sulfur_dioxide = float(request.form['free_sulfur_dioxide'])
        total_sulfur_dioxide = float(request.form['total_sulfur_dioxide'])
        density = float(request.form['density'])
        pH = float(request.form['pH'])
        sulphates = float(request.form['sulphates'])
        alcohol = float(request.form['alcohol'])
        
        # Prepare data for prediction
        features = np.array([[fixed_acidity, volatile_acidity, citric_acid, residual_sugar,
                              chlorides, free_sulfur_dioxide, total_sulfur_dioxide, density,
                              pH, sulphates, alcohol]])

        # Make prediction
        predicted_quality = model.predict(features)[0]

        return jsonify({'predicted_quality': round(predicted_quality, 2)})
    
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)
