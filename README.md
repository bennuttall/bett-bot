# BETT Bot

Raspberry Pi photo tweeting web app for BETT 2015

## Installing

Make sure you have enabled your camera first. You can do this by running `sudo raspi-config` and selecting the `Enable camera software` option.

Install the requirements:

```bash
sudo apt-get install python-pip
sudo pip install flask
```

Download the repo:

```bash
wget https://github.com/bennuttall/bett-bot/archive/master.tar.gz
tar xzf master.tar.gz
cd bett-bot-master
```

(or use `git clone`):

```bash
git clone https://github.com/bennuttall/bett-bot
cd bett-bot
```

Run the web app:

```bash
python app.py
```

## Twitter

To use the Twitter feature (tweet a picture), add your Twitter API keys from [dev.twitter.com](https://dev.twitter.com/) to `auth.py`.
