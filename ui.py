# type: ignore
import streamlit as st
import requests

# Set page layout and title
st.set_page_config(page_title="Uber Price Predictor", layout="centered")
st.title("🚗 Uber Price Estimation")

st.markdown("Enter your trip details below to calculate the estimated fare.")

# Create the form layout matching your Pydantic input features
with st.form("prediction_form"):
    col1, col2 = st.columns(2)
    
    with col1:
        vehicle_type = st.selectbox("Vehicle Type", ["UberX", "UberXL", "UberComfort"])
        pickup_location = st.text_input("Pickup Location", "Downtown")
        drop_location = st.text_input("Drop Location", "Airport")
        ride_distance = st.number_input("Ride Distance (Miles)", min_value=0.1, value=5.0)
        distance_km = ride_distance * 1.60934  # Automated calculation
        
    with col2:
        hour = st.slider("Hour of Day", 0, 23, 12)
        day_of_week = st.slider("Day of Week (0=Mon, 6=Sun)", 0, 6, 2)
        surge_multiplier = st.slider("Surge Multiplier", 1.0, 3.0, 1.0, step=0.1)
        trip_duration_min = st.number_input("Est. Duration (Minutes)", min_value=1, value=15)

    # Hidden or calculated technical parameters required by your pipeline
    avg_vtat = 5.0
    avg_ctat = 4.5
    driver_ratings = 4.8
    customer_rating = 4.9
    payment_method = "Card"
    is_weekend = 1 if day_of_week >= 5 else 0
    is_peak_hour = 1 if hour in [7, 8, 9, 16, 17, 18] else 0
    pickup_freq = 120.0

    # Submit button
    submit_button = st.form_submit_button("Estimate Fare")

if submit_button:
    # Construct payload using the expected Pydantic aliases
    payload = {
        "Vehicle Type": vehicle_type,
        "Pickup Location": pickup_location,
        "Drop Location": drop_location,
        "Avg VTAT": avg_vtat,
        "Avg CTAT": avg_ctat,
        "Ride Distance": ride_distance,
        "Driver Ratings": driver_ratings,
        "Customer Rating": customer_rating,
        "Payment Method": payment_method,
        "distance_km": distance_km,
        "hour": hour,
        "day_of_week": day_of_week,
        "is_weekend": is_weekend,
        "is_peak_hour": is_peak_hour,
        "pickup_freq": pickup_freq,
        "trip_duration_min": trip_duration_min,
        "surge_multiplier": surge_multiplier
    }
    
    try:
        # Send data to your running FastAPI container network
        response = requests.post("http://backend:8000/predict", json=payload)
        if response.status_code == 200:
            result = response.json()
            fare = result["predicted_price"]
            st.success(f"### Estimated Fare: KES {fare:,.2f}")
        else:
            st.error(f"API Error: {response.text}")
    except requests.exceptions.ConnectionError:
        st.error("Could not connect to FastAPI server. Ensure your Docker container is running.")