from __future__ import print_function
import os
import json

gmaps_api_token = os.environ['GMAPS_DISTANCE_API_KEY']
gmaps_url_base = 'https://maps.googleapis.com/maps/api/distancematrix/json?'
parsed_message = {"start_destination":"", "end_destination":""}

def format_message(event_body):
    message = event_body
    message = message.replace("+", " ")
    message = message.replace("%7C", "|")
    message = message.replace("%2C", ",")
    return message

def parse_message(event):
    event_body_formated = format_message(event['Body'])
    print(event_body_formated)
    event_body_split = event_body_formated.split("|")

    parsed_message['start_destination'] = event_body_split[0]
    parsed_message['end_destination'] = event_body_split[1]
    print(parsed_message)


def lambda_handler(event, context):
    print("Received event: " + str(event))
    parse_message(event)

    return '<?xml version=\"1.0\" encoding=\"UTF-8\"?>'\
          '<Response><Message>From: '+ str(parsed_message['start_destination']) + ' To: ' + str(parsed_message['end_destination']) +'</Message></Response>'
