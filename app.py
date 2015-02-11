from flask import Flask, render_template
from picamera import PiCamera
from glob import glob
from datetime import datetime
import os

try:
    from twython import Twython
except:
    Twython = None
    twitter = None

if Twython:
    from auth import (
        consumer_key,
        consumer_secret,
        access_token,
        access_token_secret
    )

    twitter = Twython(
        consumer_key,
        consumer_secret,
        access_token,
        access_token_secret
    )

app = Flask(__name__)

path = os.path.dirname(os.path.realpath(__file__))

def get_photos():
    photo_files = glob("%s/static/photos/*.jpg" % path)
    photos = ["/static/photos/%s" % photo.split('/')[-1] for photo in photo_files]
    return sorted(photos, reverse=True)

@app.route('/')
def index():
    photos = get_photos()
    return render_template('index.html', photos=photos)

@app.route('/capture/')
def capture():
    timestamp = datetime.now().isoformat()
    photo_path = '%s/static/photos/%s.jpg' % (path, timestamp)
    with PiCamera() as camera:
        camera.hflip = camera.vflip = True
        camera.resolution = (640, 400)
        camera.capture(photo_path)
    photos = get_photos()
    return render_template('index.html', photos=photos)

@app.route('/view/<photo>/')
def view(photo):
    return render_template('view.html', photo=photo)

@app.route('/tweet/<photo>/')
def tweet(photo):
    photo_path = '%s/static/photos/%s.jpg' % (path, photo)
    message = "I'm at the @Raspberry_Pi stand at #bett2015"
    with open(photo_path, 'rb') as media:
        twitter.update_status_with_media(status=message, media=media)
    return render_template('view.html', photo=photo, tweeted=True)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
