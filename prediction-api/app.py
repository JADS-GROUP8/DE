import os

from flask import Flask, request

from heart_disease_predictor import HeartDiseasePredictor

app = Flask(__name__)
app.config["DEBUG"] = True


@app.route('/heart_disease_predictor/', methods=['POST']) 
def predict_str():
    # the prediction input data in the message body as a JSON payload
    prediction_inout = request.get_json()
    return dp.predict_single_record(prediction_inout)


dp = HeartDiseasePredictor()
# The code within this conditional block will only run the 
# python file is executed as a script
if __name__ == '__main__':
    app.run(port=int(os.environ.get("PORT", 5000)), host='0.0.0.0', debug=True)

