import os
import pickle
import pandas as pd
from flask import jsonify
import logging


class HeartDiseasePredictor:
    def __init__(self):
        # Initialize the model attribute to None
        self.model = None

    def load_model(self, file_path):
        # Load the model from the specified file path using pickle
        with open(file_path, "rb") as file:
            return pickle.load(file)

    def predict_single_record(self, prediction_input):
        # Log the prediction input for debugging purposes
        logging.debug(prediction_input)
        # Check if the model is already loaded in
        if self.model is None:
            try:
                model_repo = os.environ["MODEL_REPO"]
                file_path = os.path.join(model_repo, "heart_disease_model.pkl")
                self.model = self.load_model(file_path)
            except KeyError:
                print("MODEL_REPO is undefined")
                self.model = self.load_model("heart_disease_model.pkl")
        # Convert the prediction input to a DataFrame
        feature_order = list(self.model.feature_names_in_)
        df = pd.DataFrame([prediction_input], columns=feature_order)
        # Make a prediction using the loaded model
        y_pred = self.model.predict(df)
        # Return the prediction outcome as a JSON message
        # with HTTP status code 200
        return jsonify({"result": str(y_pred[0])}), 200
