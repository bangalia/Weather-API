import os
import requests 

from flask import Flask, render_template,request
from pprint import PrettyPrinter
from dotenv import load_dotenv

################################################################################
## SETUP
################################################################################

app = Flask(__name__)

# Get the API key from the '.env' file
load_dotenv()
API_KEY = os.getenv('API_KEY')

pp = PrettyPrinter(indent=4)


################################################################################
## ROUTES
################################################################################

@app.route('/')
def home():
    """Displays the homepage with form for current data."""
    return render_template('home.html')

def get_letter_for_units(units):
    """Returns a user's mood."""
    return 

@app.route('/results')
def results():
    """Displays results for current weather conditions."""
    # Use 'request.args' to retrieve the city & units from the query
    # parameters.
    city = request.args.get('city')
    mood = request.args.get('mood')
    units = request.args.get('units')

    url = 'http://api.openweathermap.org/data/2.5/weather'
    params = {
        'apiid': '81e31261dddca904b71ade224b3ab056',
        'city': 'city',
        'units': 'imperial'
    }

    result_json = requests.get(url, params=params).json()


    context = {
        'date': datetime.now(),
        'city': city,
        'description': result_json['weather']['description'],
        'temp': result_json['main']['temp'],
        'humidity': result_json['main']['humidity'],
        'wind_speed': result_json['wind'][1],
        'sunrise': datetime.fromtimestamp(result_json['sys']['sunrise']),
        'sunset': datetime.fromtimestamp(result_json['sys']['sunset']),
        'units_letter': get_letter_for_units(units),
        'mood': mood
    }

    return render_template('results.html', **context)
