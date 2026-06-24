from fastapi import FastAPI
import pandas as pd
import joblib
import uvicorn
from pydantic import BaseModel, Field
from fastapi import HTTPException


app = FastAPI()
model = joblib.load("model.pkl")

# Define the exact input features expected by the model
class RideInput(BaseModel):
    vehicle_type: str = Field(..., alias="Vehicle Type")
    pickup_location: str = Field(..., alias="Pickup Location")
    drop_location: str = Field(..., alias="Drop Location")
    avg_vtat: float = Field(..., alias="Avg VTAT")
    avg_ctat: float = Field(..., alias="Avg CTAT")
    ride_distance: float = Field(..., alias="Ride Distance")
    driver_ratings: float = Field(..., alias="Driver Ratings")
    customer_rating: float = Field(..., alias="Customer Rating")
    payment_method: str = Field(..., alias="Payment Method")
    distance_km: float
    hour: int
    day_of_week: int
    is_weekend: int
    is_peak_hour: int
    pickup_freq: float
    trip_duration_min: float
    surge_multiplier: float

# Define a Prediction Endpoint - this endpoint will accept a POST request with the input data and return the predicted price
@app.post("/predict")
def predict_price(data: RideInput):
    try:
        # Convert Pydantic object to a dictionary using structural aliases
        input_dict = data.model_dump(by_alias=True)
        
        # Inject placeholder values for structural columns expected by the Pipeline
        input_dict.update({
            "Booking Status": "Completed",
            "Booking Value": 0.0,
            "Date": "2026-06-24",
            "Time": "12:00:00",
            "Booking ID": "PLACEHOLDER",
            "Customer ID": "PLACEHOLDER"
        })
        
        # Convert to DataFrame
        input_data = pd.DataFrame([input_dict])
        
        # Run inference via the pipeline
        prediction = model.predict(input_data)
        
        return {"predicted_price": float(prediction[0])}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

# Return a simple message at the root endpoint
@app.get("/")
def read_root():
    return {"message": "Welcome to the Uber Price Prediction API!"}


# Run the FastAPI application
if __name__ == "__main__":
    uvicorn.run("app:app", host="0.0.0.0", port=8000)