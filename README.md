# Weather CLI Tool

A simple Python command-line tool to fetch the current weather for any city using the OpenWeatherMap API.

## Features

- Get current temperature in Celsius.
- See weather conditions (e.g., clear sky, few clouds).
- Check humidity percentage.
- Easy-to-use command-line interface.

## Setup Instructions

### 1. Get an API Key

1.  Go to [OpenWeatherMap](https://openweathermap.org/) and sign up for a free account.
2.  Navigate to the [API Keys](https://home.openweathermap.org/api_keys) section.
3.  Copy your default key (or generate a new one).

### 2. Configure the API Key (Choose One Method)

#### Method A: Environment Variable (Recommended - More Secure)
Add the API key to your environment variables.

**On Linux/macOS:**
Add this line to your `~/.bashrc` or `~/.zshrc` file:
```bash
export OWM_API_KEY='your_api_key_here'
