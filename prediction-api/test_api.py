import pytest
from app import app


@pytest.fixture
def client():
    with app.test_client() as client:
        yield client


def test_prediction_endpoint(client):
    # Define the input data
    input_data = {
        "Age": 0,
        "Sex": 0,
        "ChestPainType": 0,
        "Cholesterol": 0,
        "FastingBS": 0,
        "MaxHR": 0,
        "ExerciseAngina": 0,
        "Oldpeak": 0.0,
        "ST_Slope": 0,
    }

    # Make a POST request to the prediction endpoint
    response = client.post("/heart_disease_predictor/", json=input_data)

    # Assert the response status code
    assert response.status_code == 200

    # Optionally, assert expected keys/values in the JSON response
    json_data = response.get_json()
    assert "result" in json_data  # Assuming the endpoint returns
