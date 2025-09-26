#!/usr/bin/env python3
"""
Weather CLI Tool
Fetches current weather data for a given city using the OpenWeatherMap API.
"""

import requests
import argparse
import os
from configparser import ConfigParser

def get_api_key():
    """Fetches the API key from a configuration file."""
    config = ConfigParser()
    config.read('config.ini')
    
    # Try to get the key from the environment variable first (more secure)
    api_key = os.environ.get('OWM_API_KEY')
    if api_key:
        return api_key
        
    # If not found, try the config file
    try:
        api_key = config['openweathermap']['api_key']
    except KeyError:
        print("Error: API key not found.")
        print("Please set the OWM_API_KEY environment variable or add it to config.ini.")
        exit(1)
    return api_key

def get_weather_data(city_name, api_key):
    """Makes the API request and returns the JSON data."""
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': city_name,
        'appid': api_key,
        'units': 'metric'  # Get temperature in Celsius
    }

    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()  # Raises an exception for bad status codes (4xx, 5xx)
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching weather data: {e}")
        exit(1)

def display_weather(weather_data):
    """Parses and displays the weather data in a readable format."""
    city = weather_data['name']
    country = weather_data['sys']['country']
    temp = weather_data['main']['temp']
    desc = weather_data['weather'][0]['description'].title()
    humidity = weather_data['main']['humidity']

    print(f"\nWeather in {city}, {country}:")
    print(f"  Temperature: {temp}°C")
    print(f"  Conditions: {desc}")
    print(f"  Humidity: {humidity}%")

def main():
    """Main function to handle command-line arguments and orchestrate the program."""
    parser = argparse.ArgumentParser(description='Get the current weather for a city.')
    parser.add_argument('city', type=str, help='Name of the city to check (e.g., "London" or "New York")')
    args = parser.parse_args()

    api_key = get_api_key()
    weather_data = get_weather_data(args.city, api_key)
    display_weather(weather_data)

if __name__ == '__main__':
    main()