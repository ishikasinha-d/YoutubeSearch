import os
import pip._vendor.requests as requests
from flask import Blueprint, render_template, current_app
from isodate import parse_duration
from .extensions import mongo

main = Blueprint('main', __name__)


@main.route('/')
def index():

    search_url= 'https://www.googleapis.com/youtube/v3/search'
    video_url = 'https://www.googleapis.com/youtube/v3/videos'

    search_params={
        'key': os.getenv('API_KEY'),
        'q': 'Cricket',  
        'part': 'snippet',
        'maxresults': 30
    }
    r= requests.get(search_url, params=search_params)

    results = r.json()['items']

    video_ids = [ result['id']['videoId'] for result in results if result['id']['kind'] == 'youtube#video']

    video_params = {
            'key' : os.getenv('API_KEY'),
            'id' : ','.join(video_ids),
            'part' : 'snippet,contentDetails',
            'maxResults' : 30
        }

    videos=[]
    r = requests.get(video_url, params=video_params)
    results = r.json()['items']
    for result in results:
        video_data = {
            'id' : result['id'],
            'url' : f'https://www.youtube.com/watch?v={ result["id"] }',
            'thumbnail' : result['snippet']['thumbnails']['high']['url'],
            'publishedAt': result['snippet']['publishedAt'],
            'duration' : int(parse_duration(result['contentDetails']['duration']).total_seconds() // 60),
            'title' : result['snippet']['title'],
        }
        videos.append(video_data)

    video_data_collection= mongo.db.video_data
    video_data_collection.insert(videos)
    video_coll= video_data_collection.find()


    return render_template('index.html', videos=video_coll)