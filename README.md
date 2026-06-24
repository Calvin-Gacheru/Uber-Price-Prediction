# End-to-End Uber Price Prediction & Production MLOps Pipeline

A production-ready machine learning and MLOps engineering project that predicts Uber ride prices using an optimized Random Forest Regressor. The project moves from raw data processing to an enterprise-grade multi-container architecture, featuring an automated CI/CD pipeline, a robust FastAPI backend with Pydantic validation, and an interactive Streamlit user interface.

---

## Architecture Overview

The system utilizes a decoupled microservices architecture orchestrating a frontend web client and a machine learning inference engine within an isolated network.

---

## 1. Data Engineering & Modeling Lifecycle

### Data Cleaning & Feature Engineering
* **Data Selection:** Processed 93,000 corporate ride records.
* **Structural Cleaning:** Dropped structural nulls (`Cancelled Rides by Customer`, `Incomplete Rides Reason`) and uniquely identifying metadata columns (`Booking ID`, `Customer ID`) to prevent overfitting.
* **Temporal Feature Extraction:** Extracted `hour`, `day_of_week`, `is_weekend`, and `is_peak_hour` from raw timestamp fields.
* **Spatial Feature Extraction:** Computed `distance_km` metrics and engineered location frequency tracking values (`pickup_freq`).

### Model Training & Robust Validation
* **Inference Pipeline:** Bundled data transformations (`ColumnTransformer`, `StandardScaler`, `OneHotEncoder`) directly into a scikit-learn `Pipeline` object to permanently prevent inference-time data leakage.
* **Algorithm:** Trained a `RandomForestRegressor` with restricted tree structures to avoid leaf-node overfitting.
* **Validation Strategy:** Implemented strict 5-Fold Cross-Validation to evaluate real-world generalization stability.

**Cross-Validation Evaluation Metrics:**
* **Scores per Fold:** `[0.9836, 0.9851, 0.9879, 0.9824, 0.9881]`
* **Average $R^2$ Score:** `0.9854` (98.54% variance explained)
* **Standard Deviation:** `0.0023` (High system stability across splits)

---

## 2. Model Serving Layer (FastAPI Backend)

The trained pipeline is persisted via `joblib` into a high-performance REST API built using **FastAPI**. 
* **Data Integrity:** Strict data-typing enforced by a Pydantic `BaseModel` schema with data mapping aliases matching the original enterprise data storage configuration.
* **Crash Resilience:** Implemented internal exception handlers preventing raw traceback leaks.

---

## 3. Interactive Client Layer (Streamlit UI)

An intuitive graphical dashboard designed using **Streamlit** to mimic the consumer-facing Uber ride configuration experience. It calculates user inputs dynamically, structures the API-compliant JSON payload, runs external async HTTP POST requests to the inference container, and updates fares in real time.

---

## 4. Multi-Container Orchestration (Docker & UV)

To secure total parity across dev and cloud environments, both microservices are strictly containerized using lightweight Python base footprints and **Astral UV** for blistering package resolution.

### System Prerequisites
* Docker Engine installed
* Docker Compose V2 plugin configured

### Build and Run Pipeline

Initialize the complete interconnected application network with a single command:
```bash
docker compose up --build
```

- Backend Engine: http://localhost:8000 (Swagger UI Documentation at /docs)
- Frontend Interface: http://localhost:8501

## 5. Continuous Integration (CI/CD Workflow)

Automated build operations are integrated using GitHub Actions. Every code modifications push or Pull Request sent to the main branch spins up a fresh ubuntu-latest workspace, clones the codebase, parses structural integrity, and validates the build sequence of the Docker containers.
```yaml
# .github/workflows/ci.yml
name: CI Pipeline
on:
  push:
    branches: [main]
  pull_request:
    branches: [main]

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Build Docker Image
        run: docker build -t uber-price-api .
```
## Project Repository Structure

```Plaintext
├── .github/
│   └── workflows/
│       └── ci.yml             # GitHub Actions continuous integration pipeline
├── app.py                     # FastAPI production model server
├── ui.py                      # Streamlit graphical client application
├── model.pkl                  # Serialized Scikit-Learn preprocessing & training pipeline
├── Dockerfile                 # Backend microservice blueprint 
├── Dockerfile.ui              # Frontend client microservice blueprint
├── docker-compose.yml         # Container runtime mesh config file
├── requirements.txt           # Explicit system deployment dependencies
└── README.md
```