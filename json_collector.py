import requests
import json
from datetime import datetime
from concurrent.futures import ThreadPoolExecutor
import os
from bs4 import BeautifulSoup

API_KEY = "4e7f010786af1678240419e281bcdad9"

cities = [
    {"name": "Amman", "lat": 31.9552, "lon": 35.9450},
    {"name": "As Salt", "lat": 32.0392, "lon": 35.7272},
    {"name": "Irbid", "lat": 32.5569, "lon": 35.8497},
    {"name": "Zarqa", "lat": 32.0728, "lon": 36.0870},
    {"name": "Aqaba", "lat": 29.5320, "lon": 35.0063},
    {"name": "Mafraq", "lat": 32.3417, "lon": 36.2028}
]

def scrape_weather_info(city_name):
    try:
        url = f"https://www.timeanddate.com/weather/jordan/{city_name.lower().replace(' ', '-')}"
        page = requests.get(url, timeout=5)
        soup = BeautifulSoup(page.content, "html.parser")
        temp_tag = soup.find("div", class_="h2")
        temp = float(temp_tag.text.strip().replace("°C","")) if temp_tag and temp_tag.text.strip() else None
        return {"scraped_temp_C": temp}
    except Exception:
        return {"scraped_temp_C": None}

def fetch_weather(city):
    try:
        url = f"https://api.openweathermap.org/data/2.5/weather?lat={city['lat']}&lon={city['lon']}&appid={API_KEY}&units=metric"
        r = requests.get(url, timeout=5).json()
        temp = r.get("main", {}).get("temp")
        humidity = r.get("main", {}).get("humidity")
        wind_speed = r.get("wind", {}).get("speed")
        desc = r.get("weather", [{}])[0].get("description")
        scrape_data = scrape_weather_info(city["name"])
        return {
            "city_name": city["name"],
            "date": datetime.utcnow().strftime("%Y-%m-%d"),
            "temp_C": temp,
            "humidity": humidity,
            "wind_speed": wind_speed,
            "desc": desc,
            **scrape_data
        }
    except Exception:
        return {
            "city_name": city["name"],
            "date": datetime.utcnow().strftime("%Y-%m-%d"),
            "temp_C": None,
            "humidity": None,
            "wind_speed": None,
            "desc": None,
            "scraped_temp_C": None
        }

def collect_and_save_daily(filename="weather_history.json"):
    with ThreadPoolExecutor() as executor:
        results = list(executor.map(fetch_weather, cities))

    if os.path.exists(filename):
        try:
            with open(filename, "r", encoding="utf-8") as f:
                old_data = json.load(f)
            results = old_data + results
        except Exception:
            print("⚠️ Old JSON file is corrupted, will overwrite.")

    with open(filename, "w", encoding="utf-8") as f:
        json.dump(results, f, indent=2, ensure_ascii=False)
    print(f"✅ Data saved in {filename}")
    return filename

if __name__ == "__main__":
    collect_and_save_daily()
