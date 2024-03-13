from slack_sdk import WebClient
import os
import json


class Slack_MESSAGE(object):

    def load_config():
        with open('Slack/config.json') as config_file:
            config = json.load(config_file)
        return config.get('slack_api_token')

    def Send_message(message:str):
        slack_api_token = Slack_MESSAGE.load_config()
        if slack_api_token is None:
            raise ValueError("Slack API token not found in configuration file") # Initialize Slack client with your API token
        client = WebClient(token=slack_api_token)

        #   Define the channel where you want to send the message
        channel = "#bus-alerts"

        # Send the message to the channel
        response = client.chat_postMessage(channel=channel, text=message)

        # Check if the message was successfully sent
        if response["ok"]:
            return True
        else:
            return False
            