import pandas as pd
import numpy as np
import json
from sklearn.preprocessing import LabelEncoder, MinMaxScaler

JSON_FILE = "weather_history.json"

def load_weather_history(filename=JSON_FILE):
    try:
        with open(filename, "r", encoding="utf-8") as f:
            data = json.load(f)
        return pd.DataFrame(data)
    except Exception:
        print("⚠️ JSON file is empty or corrupted.")
        return pd.DataFrame()

def predict_next_week(df, city_name):
    city_data = df[df["city_name"] == city_name].copy()
    if city_data.empty:
        print(f"⚠️ No data available for {city_name}")
        return pd.DataFrame()

    city_data = city_data.dropna(subset=["temp_C", "humidity", "wind_speed"])
    if city_data.empty:
        print(f"⚠️ All data for {city_name} contains missing values.")
        return pd.DataFrame()

    le = LabelEncoder()
    city_data["desc_encoded"] = le.fit_transform(city_data["desc"].fillna("unknown"))
    scaler = MinMaxScaler()
    city_data[["temp_C", "humidity", "wind_speed"]] = scaler.fit_transform(
        city_data[["temp_C", "humidity", "wind_speed"]]
    )


    temp_avg = city_data["temp_C"].mean() * 30
    humidity_avg = city_data["humidity"].mean() * 100
    wind_avg = city_data["wind_speed"].mean() * 10

    predictions = []
    for day in range(1, 8):
        predictions.append({
            "city_name": city_name,
            "day": f"Day+{day}",
            "pred_temp_C": round(temp_avg + np.random.uniform(-1, 1), 1),
            "pred_humidity": round(humidity_avg + np.random.uniform(-2, 2), 1),
            "pred_wind_speed": round(wind_avg + np.random.uniform(-0.5, 0.5), 1)
        })
    return pd.DataFrame(predictions)

if __name__ == "__main__":
    df = load_weather_history(JSON_FILE)
    if df.empty:
        print("⚠️ No data available to analyze.")
    else:
        cities_list = df["city_name"].unique()
        for city in cities_list:
            print(f"\n Predictions for {city}:")
            week_pred = predict_next_week(df, city)
            print(week_pred.to_string(index=False))
