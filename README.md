# Reddit saves to markdown

Download all your reddit saves to markdown. 

## Pre-requisites
- [ ] Create a reddit "script only" developer app in https://www.reddit.com/prefs/apps
- [ ] Have python3 installed and do `pip3 install praw dotenv-python`

## Instructions

1. Create an .env file in the project (rename the .env.example to .env) with your client id, secret, username and password.
2. Run `python3 download_favorites.py`
3. Done!

Note, this doesn't work with 2FA (I had to disable 2FA)

