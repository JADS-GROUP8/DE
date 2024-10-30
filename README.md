# DE Assignment 1

## Project Overview

This project is a heart disease prediction application consisting of two main components: a prediction API and a user interface (UI). The prediction API uses a machine learning model to predict the likelihood of heart disease based on user input, while the UI provides a web interface for users to input their data and view the prediction results.

## Folder Structure

```
.github/                    # GitHub Actions workflows for CI/CD
cloud-build/                # Cloud Build configuration files
prediction-api/             # Source code and dependencies for the prediction API
prediction-ui/              # Source code and dependencies for the user interface
vertex-ai/                  # Vertex AI pipeline related files (notebook and yaml)
docker-compose.yaml         # Docker Compose configuration file
parameters.json.example     # Example parameters file
README.md                   # Project README file
```

## How to Run the Project

### Prerequisites

- Docker
- Docker Compose

### Steps to Run

1. **Clone the repository**:

   ```sh
   git clone https://github.com/JADS-GROUP8/DE
   cd de
   ```

2. **Build and run the application using Docker Compose**:

   ```sh
   docker-compose up --build
   ```

3. **Access the application**:
   - The prediction API will be available at `http://localhost:5000`.
   - The user interface will be available at `http://localhost:5001/checkheartdisease`.

### Testing

To run the tests for the prediction API, use the following command:

```sh
cd prediction-api
pytest test_api.py
```

## Deployment

The project includes Cloud Build configurations for deploying the application to Google Cloud Run. The deployment steps are defined in the `cloud-build/cloud_build_app_deployment_execution.json` file.
