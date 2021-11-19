import os
import pip._vendor.requests as requests
from flask import Blueprint, render_template, current_app

main = Blueprint('main', __name__)

@main.route('/')
def index():

    search_url= 'https://www.googleapis.com/youtube/v3/search'

    search_params={
        'key': os.getenv('API_KEY'),
        'q': 'python',
        'part': 'snippet',
        'maxresults': 9
    }
    r= requests.get(search_url, params=search_params)

    print(r.text)

    return render_template('index.html')