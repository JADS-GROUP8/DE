import os
import json
import pickle
import numpy as np

class HeartDiseasePredictor:
    def __init__(self):
        self.model = None
        self.load_model()

    def load_model(self, file_path=None):
        if file_path is None:
            try:
                model_repo = os.environ['MODEL_REPO']
                file_path = os.path.join(model_repo, "heart_disease_model.pkl")
            except KeyError:
                print("MODEL_REPO is undefined")
                file_path = 'C:\Checkouts\.JADS\DE\prediction-api\heart_disease_model.pkl'
        
        with open(file_path, 'rb') as file:
            self.model = pickle.load(file)

    def predict(self, input_json):
        if self.model is None:
            raise Exception("Model is not loaded")

        input_data = json.loads(input_json)
        input_array = np.array([input_data[key] for key in sorted(input_data.keys())]).reshape(1, -1)
        prediction = self.model.predict(input_array)
        return prediction[0]

# Example usage
if __name__ == "__main__":
    predictor = HeartDiseasePredictor()
    sample_json = '''{
  "age": 45,
  "sex": 0,
  "chest_pain": 0,
  "cholesterol": 289,
  "fasting_bs": 0,
  "max_hr": 172,
  "exercise_angina": 0,
  "old_peak": 0,
  "st_slope": 0
}'''
    prediction = predictor.predict(sample_json)
    print(f"Prediction: {prediction}")