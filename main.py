#!/usr/bin/python
import requests
import json
from twilio.rest import TwilioRestClient

def get_config():
	data = open("config.json", "r")
	data_json = json.load(data)
	data.close()
	return data_json 

def git_connect(config):
	events = requests.get("https://api.github.com/notifications?access_token=%s" %config['access_token'])
	events = json.loads(events.text)
	if(events):
		subject=events[0]['subject']['title']
		repo_name=events[0]['repository']['full_name']
		message = "You got a new notifcation \n Repo: "+repo_name+" \n Subject: "+ subject
	else:
		message= "No new notification "
	return message

def send_sms(config, message):
	account_sid = config['sid']
	auth_token = config['token']
	client = TwilioRestClient(account_sid, auth_token)
	send = client.messages.create(to=config['to_number'], from_=config['from_number'], body=message)


def main():
	config = get_config()
	message = git_connect(config['github'])
	send_sms(config['twilio'],message)

if __name__ == "__main__":
    main()
