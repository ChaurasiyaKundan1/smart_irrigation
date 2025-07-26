import requests
import random

# API key and city details
API_KEY = "224f09c28c5637219320b7857e880602"
CITY = "Kathmandu"
URL = f"http://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric"

def get_weather():
    try:
        response = requests.get(URL)
        response.raise_for_status()
        data = response.json()
        weather = {
            "temperature": data["main"]["temp"],
            "humidity": data["main"]["humidity"]
        }
        return weather
    except requests.exceptions.RequestException as e:
        print("Error fetching weather:", e)
        return None
    except KeyError:
        print("Unexpected response format:", response.json())
        return None

def get_soil_moisture():
    # Simulated soil moisture sensor reading (0–100%)
    return random.randint(10, 90)

def decide_irrigation(temperature, humidity, soil_moisture):
    if soil_moisture < 30 and temperature > 25:
        return "Irrigation needed!"
    else:
        return "No irrigation needed."

def main():
    weather = get_weather()
    if weather:
        soil_moisture = get_soil_moisture()
        print(f"Temperature: {weather['temperature']}°C")
        print(f"Humidity: {weather['humidity']}%")
        print(f"Soil Moisture: {soil_moisture}%")
        decision = decide_irrigation(weather['temperature'], weather['humidity'], soil_moisture)
        print("System Decision:", decision)

if __name__ == "__main__":
    main()


