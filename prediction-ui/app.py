import os
import logging
import requests
from flask import Flask, request, render_template, jsonify

# Initialize Flask app
app = Flask(__name__)


@app.route("/checkheartdisease", methods=["GET", "POST"])
def check_heart_disease():
    if request.method == "GET":
        return render_template("input_form_page.html")

    elif request.method == "POST":
        # Collect input data from the form
        prediction_input = {
            "Age": int(request.form.get("age")),
            "Sex": int(request.form.get("sex")),
            "ChestPainType": int(request.form.get("chestpain")),
            "Cholesterol": int(request.form.get("cholesterol")),
            "FastingBS": int(request.form.get("fastingbs")),
            "MaxHR": int(request.form.get("maxhr")),
            "ExerciseAngina": int(request.form.get("exerciseangina")),
            "Oldpeak": float(request.form.get("oldpeak")),
            "ST_Slope": int(request.form.get("stslope")),
        }

        # Get the predictor API URL from environment variables
        predictor_api_url = os.environ["PREDICTOR_API"]

        # Send a POST request to the prediction API
        res = requests.post(predictor_api_url, json=prediction_input)

        if res.status_code != 200:
            return jsonify(message="Prediction API failed"), 500

        # Extract prediction result from the API response
        prediction_value = int(res.json().get("result"))

        logging.info(
            "Prediction Input: %s, Prediction Output: %s",
            prediction_input,
            prediction_value,
        )

        return render_template(
            "response_page.html", prediction_variable=prediction_value
        )

    else:
        return jsonify(message="Method Not Allowed"), 405


if __name__ == "__main__":
    # Run the Flask app
    app.run(port=int(os.environ.get("PORT", 5000)), host="0.0.0.0", debug=True)
