# type: ignore
import pandas as pd
import numpy as np

RANDOM_STATE = 42
rng = np.random.default_rng(RANDOM_STATE)

DATA_PATH = "data/Uber Data.csv"          
OUTPUT_PATH = "data/Uber_Data_simulated_fare.csv"

# LOCATION COORDINATE LOOKUP
LOCATION_COORDS = {
    "AIIMS": (28.5672, 77.2100), "Adarsh Nagar": (28.7170, 77.1700),
    "Akshardham": (28.6127, 77.2773), "Ambience Mall": (28.5020, 77.0950),
    "Anand Vihar": (28.6470, 77.3160), "Anand Vihar ISBT": (28.6480, 77.3150),
    "Ardee City": (28.4350, 77.0290), "Arjangarh": (28.5070, 77.1530),
    "Ashok Park Main": (28.6720, 77.1490), "Ashok Vihar": (28.6960, 77.1820),
    "Ashram": (28.5777, 77.2545), "Aya Nagar": (28.4738, 77.1297),
    "Azadpur": (28.7070, 77.1750), "Badarpur": (28.4930, 77.3030),
    "Badshahpur": (28.4080, 77.0700), "Bahadurgarh": (28.6930, 76.9350),
    "Barakhamba Road": (28.6290, 77.2255), "Basai Dhankot": (28.4660, 76.9800),
    "Bhikaji Cama Place": (28.5727, 77.1880), "Bhiwadi": (28.2100, 76.8700),
    "Botanical Garden": (28.5640, 77.3340), "Central Secretariat": (28.6140, 77.2120),
    "Chanakyapuri": (28.5933, 77.1900), "Chandni Chowk": (28.6505, 77.2303),
    "Chhatarpur": (28.4950, 77.1820), "Chirag Delhi": (28.5410, 77.2350),
    "Civil Lines Gurgaon": (28.4700, 77.0260), "Connaught Place": (28.6315, 77.2167),
    "Cyber Hub": (28.4950, 77.0890), "DLF City Court": (28.4810, 77.0950),
    "DLF Phase 3": (28.4880, 77.0930), "Delhi Gate": (28.6450, 77.2380),
    "Dilshad Garden": (28.6770, 77.3220), "Dwarka Mor": (28.6190, 77.0353),
    "Dwarka Sector 21": (28.5520, 77.0590), "Faridabad Sector 15": (28.4080, 77.3160),
    "GTB Nagar": (28.6990, 77.2080), "Ghaziabad": (28.6692, 77.4538),
    "Ghitorni": (28.4920, 77.1535), "Ghitorni Village": (28.4940, 77.1500),
    "Golf Course Road": (28.4720, 77.1010), "Govindpuri": (28.5364, 77.2589),
    "Greater Kailash": (28.5494, 77.2425), "Greater Noida": (28.4740, 77.5040),
    "Green Park": (28.5585, 77.2065), "Gurgaon Railway Station": (28.4730, 77.0180),
    "Gurgaon Sector 29": (28.4630, 77.0500), "Gurgaon Sector 56": (28.4180, 77.0960),
    "Gwal Pahari": (28.4290, 77.1450), "Hauz Khas": (28.5481, 77.2073),
    "Hauz Rani": (28.5267, 77.2110), "Hero Honda Chowk": (28.4070, 77.0480),
    "Huda City Centre": (28.4590, 77.0720), "IFFCO Chowk": (28.4720, 77.0710),
    "IGI Airport": (28.5562, 77.1000), "IGNOU Road": (28.5390, 77.1670),
    "IIT Delhi": (28.5450, 77.1925), "IMT Manesar": (28.3760, 76.9520),
    "INA Market": (28.5747, 77.2107), "ITO": (28.6280, 77.2420),
    "Inderlok": (28.6720, 77.1700), "India Gate": (28.6129, 77.2295),
    "Indirapuram": (28.6450, 77.3700), "Indraprastha": (28.6230, 77.2480),
    "Jahangirpuri": (28.7280, 77.1660), "Jama Masjid": (28.6507, 77.2334),
    "Janakpuri": (28.6219, 77.0850), "Jasola": (28.5460, 77.2890),
    "Jhilmil": (28.6750, 77.3120), "Jor Bagh": (28.5880, 77.2191),
    "Kadarpur": (28.4150, 77.1180), "Kalkaji": (28.5414, 77.2588),
    "Kanhaiya Nagar": (28.6790, 77.1620), "Karkarduma": (28.6520, 77.2950),
    "Karol Bagh": (28.6517, 77.1900), "Kashmere Gate": (28.6660, 77.2280),
    "Kashmere Gate ISBT": (28.6670, 77.2275), "Kaushambi": (28.6480, 77.3170),
    "Keshav Puram": (28.6890, 77.1600), "Khan Market": (28.6004, 77.2274),
    "Khandsa": (28.4530, 77.0080), "Kherki Daula Toll": (28.3990, 76.9920),
    "Kirti Nagar": (28.6520, 77.1450), "Lajpat Nagar": (28.5677, 77.2433),
    "Lal Quila": (28.6562, 77.2410), "Laxmi Nagar": (28.6310, 77.2770),
    "Lok Kalyan Marg": (28.6010, 77.1930), "MG Road": (28.4790, 77.0820),
    "Madipur": (28.6650, 77.1240), "Maidan Garhi": (28.4900, 77.2050),
    "Malviya Nagar": (28.5286, 77.2105), "Mandi House": (28.6260, 77.2350),
    "Manesar": (28.3540, 76.9350), "Mansarovar Park": (28.6760, 77.2900),
    "Mayur Vihar": (28.6090, 77.2920), "Meerut": (28.9845, 77.7064),
    "Mehrauli": (28.5170, 77.1840), "Model Town": (28.7110, 77.1920),
    "Moolchand": (28.5651, 77.2350), "Moti Nagar": (28.6573, 77.1463),
    "Mundka": (28.6820, 77.0310), "Munirka": (28.5550, 77.1740),
    "Narsinghpur": (28.4860, 77.1700), "Nawada": (28.5680, 77.0540),
    "Nehru Place": (28.5483, 77.2513), "Netaji Subhash Place": (28.6960, 77.1500),
    "New Colony": (28.3920, 77.3050), "New Delhi Railway Station": (28.6433, 77.2208),
    "Nirman Vihar": (28.6310, 77.2840), "Noida Extension": (28.5660, 77.4350),
    "Noida Film City": (28.5860, 77.3310), "Noida Sector 18": (28.5700, 77.3260),
    "Noida Sector 62": (28.6270, 77.3650), "Okhla": (28.5460, 77.2730),
    "Old Gurgaon": (28.4670, 77.0070), "Paharganj": (28.6440, 77.2110),
    "Palam Vihar": (28.5050, 77.0710), "Panchsheel Park": (28.5447, 77.2169),
    "Panipat": (29.3909, 76.9635), "Paschim Vihar": (28.6730, 77.1010),
    "Pataudi Chowk": (28.3450, 76.7720), "Patel Chowk": (28.6190, 77.2120),
    "Peeragarhi": (28.6710, 77.0980), "Pitampura": (28.7041, 77.1318),
    "Pragati Maidan": (28.6190, 77.2440), "Preet Vihar": (28.6360, 77.2940),
    "Pulbangash": (28.6680, 77.2080), "Punjabi Bagh": (28.6740, 77.1310),
    "Qutub Minar": (28.5245, 77.1855), "RK Puram": (28.5650, 77.1770),
    "Raj Nagar Extension": (28.7050, 77.4310), "Rajiv Chowk": (28.6328, 77.2197),
    "Rajiv Nagar": (28.4540, 77.0190), "Rajouri Garden": (28.6492, 77.1212),
    "Ramesh Nagar": (28.6536, 77.1318), "Rithala": (28.7210, 77.1080),
    "Rohini": (28.7430, 77.0670), "Rohini East": (28.7330, 77.1130),
    "Rohini West": (28.7330, 77.0890), "Sadar Bazar Gurgaon": (28.4700, 77.0270),
    "Saidulajab": (28.5160, 77.2090), "Saket": (28.5245, 77.2066),
    "Saket A Block": (28.5230, 77.2010), "Samaypur Badli": (28.7460, 77.1380),
    "Sarai Kale Khan": (28.5870, 77.2520), "Sarojini Nagar": (28.5772, 77.1962),
    "Satguru Ram Singh Marg": (28.6710, 77.2070), "Seelampur": (28.6720, 77.2730),
    "Shahdara": (28.6730, 77.2890), "Shastri Nagar": (28.6810, 77.1820),
    "Shastri Park": (28.6760, 77.2570), "Shivaji Park": (28.6680, 77.1380),
    "Sikanderpur": (28.4790, 77.0890), "Sohna Road": (28.4280, 77.0420),
    "Sonipat": (28.9930, 77.0150), "South Extension": (28.5730, 77.2230),
    "Subhash Chowk": (28.4350, 77.0480), "Subhash Nagar": (28.6388, 77.1110),
    "Sultanpur": (28.4990, 77.1740), "Sushant Lok": (28.4630, 77.0640),
    "Tagore Garden": (28.6420, 77.1090), "Tilak Nagar": (28.6378, 77.0978),
    "Tis Hazari": (28.6700, 77.2150), "Tughlakabad": (28.5090, 77.2620),
    "Udyog Bhawan": (28.6190, 77.2200), "Udyog Vihar": (28.4990, 77.0780),
    "Udyog Vihar Phase 4": (28.5040, 77.0850), "Uttam Nagar": (28.6196, 77.0560),
    "Vaishali": (28.6470, 77.3380), "Vasant Kunj": (28.5200, 77.1590),
    "Vatika Chowk": (28.4380, 77.0510), "Vidhan Sabha": (28.6670, 77.2390),
    "Vinobapuri": (28.5638, 77.2492), "Vishwavidyalaya": (28.6990, 77.2120),
    "Welcome": (28.6730, 77.2790), "Yamuna Bank": (28.6190, 77.2620),
}

# Haversine distance function
def haversine_distance(lat1, lon1, lat2, lon2):
    """Great-circle distance (km) between two lat/lon points."""
    R = 6371.0
    lat1, lon1, lat2, lon2 = map(np.radians, [lat1, lon1, lat2, lon2])
    dlat, dlon = lat2 - lat1, lon2 - lon1
    a = np.sin(dlat / 2) ** 2 + np.cos(lat1) * np.cos(lat2) * np.sin(dlon / 2) ** 2
    return R * 2 * np.arcsin(np.sqrt(a))


# Load data, minimal cleaning
df = pd.read_csv(DATA_PATH)
df["Booking ID"] = df["Booking ID"].astype(str).str.strip('"')
df = df.drop_duplicates()
df = df[df["Booking Status"] == "Completed"].copy()          # only real trips have fares
df["datetime"] = pd.to_datetime(df["Date"] + " " + df["Time"])

print(f"Rows to simulate fares for: {len(df):,}")

# Features the simulated fare will depend on
df["pickup_lat"] = df["Pickup Location"].map(lambda x: LOCATION_COORDS[x][0]) # type: ignore
df["pickup_lon"] = df["Pickup Location"].map(lambda x: LOCATION_COORDS[x][1]) # type: ignore
df["drop_lat"] = df["Drop Location"].map(lambda x: LOCATION_COORDS[x][0]) # type: ignore
df["drop_lon"] = df["Drop Location"].map(lambda x: LOCATION_COORDS[x][1]) # type: ignore
df["distance_km"] = haversine_distance(
    df["pickup_lat"], df["pickup_lon"], df["drop_lat"], df["drop_lon"]
)

df["hour"] = df["datetime"].dt.hour
df["day_of_week"] = df["datetime"].dt.dayofweek
df["is_weekend"] = (df["day_of_week"] >= 5).astype(int)
df["is_peak_hour"] = df["hour"].isin([7, 8, 9, 17, 18, 19, 20]).astype(int)
df["pickup_freq"] = df["Pickup Location"].map(df["Pickup Location"].value_counts(normalize=True))

"""Illustrative fare-structure constants (base fare, per-km rate, per-minute
rate, vehicle-class multiplier) loosely modeled on how real ride-hailing
fares are built up. These are simulation parameters for demonstration — not published Uber rates.
"""

# Per-vehicle pricing structure
PRICING = {
    "eBike":         {"base": 15, "per_km": 4.5,  "per_min": 0.5, "multiplier": 0.70},
    "Bike":          {"base": 18, "per_km": 5.0,  "per_min": 0.6, "multiplier": 0.75},
    "Auto":          {"base": 25, "per_km": 8.0,  "per_min": 1.0, "multiplier": 0.90},
    "Go Mini":       {"base": 40, "per_km": 11.0, "per_min": 1.5, "multiplier": 1.00},
    "Go Sedan":      {"base": 50, "per_km": 13.0, "per_min": 1.8, "multiplier": 1.15},
    "Premier Sedan": {"base": 65, "per_km": 16.0, "per_min": 2.2, "multiplier": 1.35},
    "Uber XL":       {"base": 80, "per_km": 19.0, "per_min": 2.5, "multiplier": 1.60},
}
pricing_lookup = df["Vehicle Type"].map(PRICING).apply(pd.Series)
df["base_fare"] = pricing_lookup["base"]
df["per_km_rate"] = pricing_lookup["per_km"]
df["per_min_rate"] = pricing_lookup["per_min"]
df["vehicle_multiplier"] = pricing_lookup["multiplier"]

# Simulate trip duration from distance + time-of-day traffic
"""
Average city driving speed, slowed during rush hour, faster late at
night with empty roads. Each ride also gets its own random congestion
jitter (log-normal, centered at 1.0) to mimic real traffic variability.
"""
BASE_SPEED_KMPH = 26.0

def hour_speed_multiplier(hour):
    if hour in (7, 8, 9, 17, 18, 19, 20):     # rush hour -> slower
        return 0.55
    elif hour in (23, 0, 1, 2, 3, 4):          # late night -> faster, empty roads
        return 1.35
    else:
        return 1.0


df["speed_multiplier"] = df["hour"].apply(hour_speed_multiplier)
traffic_jitter = rng.lognormal(mean=0.0, sigma=0.15, size=len(df))
df["effective_speed_kmph"] = (BASE_SPEED_KMPH * df["speed_multiplier"] * traffic_jitter).clip(8, 45)
df["trip_duration_min"] = (df["distance_km"] / df["effective_speed_kmph"]) * 60

# Simulate surge pricing
base_surge = 1.0 + 0.4 * df["is_peak_hour"] + 0.3 * (df["pickup_freq"] / df["pickup_freq"].max())
random_surge_event = rng.choice([1.0, 1.5, 2.0], size=len(df), p=[0.85, 0.12, 0.03])
df["surge_multiplier"] = (base_surge * random_surge_event).round(2)

# Combine into the final simulated fare
"""
fare = (base + distance*per_km_rate + duration*per_min_rate)
       * vehicle_multiplier * surge_multiplier
       +/- small random jitter (driver/route variation), floored at a
       minimum fare (mirrors the real-world ₹30-50 minimum fare floor).
"""

raw_fare = (
    df["base_fare"]
    + df["distance_km"] * df["per_km_rate"]
    + df["trip_duration_min"] * df["per_min_rate"]
) * df["vehicle_multiplier"] * df["surge_multiplier"]

fare_noise = rng.normal(loc=1.0, scale=0.05, size=len(df))   # +/- 5% random jitter
df["Simulated Booking Value"] = (raw_fare * fare_noise).clip(lower=30).round(0)

# Drop helper columns we no longer need, keep the useful new ones
df = df.drop(columns=[
    "pickup_lat", "pickup_lon", "drop_lat", "drop_lon",
    "base_fare", "per_km_rate", "per_min_rate",
    "vehicle_multiplier", "speed_multiplier", "effective_speed_kmph",
])

# Save the new dataset
df.to_csv(OUTPUT_PATH, index=False)
print(f"Saved simulated dataset to: {OUTPUT_PATH}  ({len(df):,} rows, {len(df.columns)} columns)\n")

print("Sample of original vs. simulated fare:")
print(df[["Vehicle Type", "distance_km", "trip_duration_min", "surge_multiplier",
          "Booking Value", "Simulated Booking Value"]].head(10).round(2))