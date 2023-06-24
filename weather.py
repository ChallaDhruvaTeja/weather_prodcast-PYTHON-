import json
import requests

def get_weather(city):
    API_KEY="7d292201f0b496ce47b786e3fb3e742b"
    url = "https://api.openweathermap.org/data/2.5/weather?q=hyderabad&appid=e0ed021b0f3eca365eb56858fbf52f1f"

    # url = "https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid="+API_KEY

    response = requests.get(url)
       

    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for non-2xx status codes
        data = response.json()
        
        # Extract relevant information from the response
        temperature = data['main']['temp']
        description = data['weather'][0]['description']
        humidity = data['main']['humidity']

        # Display the weather forecast
        print(f"Weather forecast for {city}:")
        print(f"Temperature: {temperature} K")
        print(f"Description: {description}")
        print(f"Humidity:{humidity}")
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
    except KeyError:
        print("Error: Invalid response received from the server.")
    except json.JSONDecodeError:
        print("Error: Failed to parse the response from the server.")

if __name__ == '__main__':
    city_name = input("Enter the name of a city: ")
    get_weather(city_name)

   
















