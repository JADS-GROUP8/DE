# importing Flask and other modules
import json
import os
import logging
import requests
from flask import Flask, request, render_template, jsonify

# Flask constructor
app = Flask(__name__)

# A decorator used to tell the application
# which URL is associated function
@app.route('/checkheartdisease', methods=["GET", "POST"])
def check_heart_disease():
    if request.method == "GET":
        return render_template("input_form_page.html")

    elif request.method == "POST":
        prediction_input = {
            "Age": int(request.form.get("age")),
            "Sex": int(request.form.get("sex")),  # Assuming 'sex' is a dropdown with index values
            "ChestPainType": int(request.form.get("chestpain")),  # Assuming 'chestpain' is a dropdown with index values
            "Cholesterol": int(request.form.get("cholesterol")),
            "FastingBS": int(request.form.get("fastingbs")),
            "MaxHR": int(request.form.get("maxhr")),
            "ExerciseAngina": int(request.form.get("exerciseangina")),  # Assuming 'exerciseangina' is a dropdown with index values
            "Oldpeak": float(request.form.get("oldpeak")),
            "ST_Slope": int(request.form.get("stslope"))  # Assuming 'stslope' is a dropdown with index values
            }
        

        logging.error("Prediction input : %s", prediction_input)

        # use requests library to execute the prediction service API by sending an HTTP POST request
        # use an environment variable to find the value of the diabetes prediction API
        # json.dumps() function will convert a subset of Python objects into a json string.
        # json.loads() method can be used to parse a valid JSON string and convert it into a Python Dictionary.
        predictor_api_url = os.environ['PREDICTOR_API']

        logging.error(prediction_input)

        res = requests.post(predictor_api_url, json=prediction_input)

        logging.error(res)

        if (res.status_code != 200):
            return jsonify(message="Prediction API failed"), 500

        prediction_value = res.json().get('result')
        logging.info("Prediction Output : %s", prediction_value)
        return render_template("response_page.html",
                               prediction_variable=prediction_value)

    else:
        return jsonify(message="Method Not Allowed"), 405  # The 405 Method Not Allowed should be used to indicate
    # that our app that does not allow the users to perform any other HTTP method (e.g., PUT and  DELETE) for
    # '/checkheartdisease' path


# The code within this conditional block will only run the python file is executed as a
# script. See https://realpython.com/if-name-main-python/
if __name__ == '__main__':
    app.run(port=int(os.environ.get("PORT", 5000)), host='0.0.0.0', debug=True)
