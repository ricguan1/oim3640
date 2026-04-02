import requests 
from pprint import pprint
from dotenv import load_dotenv
import os

load_dotenv()  # Load environment variables from .env file
API_KEY = os.getenv('OPENWEATHER_API_KEY')  # Get the API key from environment variable

url = (f'https://api.openweathermap.org/data/2.5/weather'
       f'?q=Beijing&appid={API_KEY}&units=metric')

print(url)
data = requests.get(url).json()
print(f"Beijing: {data['main']['temp']}°C")


