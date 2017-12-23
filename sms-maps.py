from __future__ import print_function
import os
import json
import urllib.request

gmaps_api_token = os.environ['GMAPS_DISTANCE_API_KEY']
gmaps_url_base = 'https://maps.googleapis.com/maps/api/distancematrix/json?'
parsed_destinations = {"start_destination":"", "end_destination":"", "formated_start_destination":"","formated_end_destination":""}

def format_destinations(event_body):
    message = event_body
    message = message.replace('+', ' ')
    message = message.replace('%7C', '|')
    message = message.replace('%2C', '')
    return message

def format_original_destinations(event_body):
    message = event_body
    message = message.replace('%2C','')
    return message

def build_parsed_destinations(event_body):
    formated_message = format_original_destinations(event_body)
    original_destinations = formated_message.split('%7C')
    parsed_destinations['start_destination'] = original_destinations[0]
    parsed_destinations['end_destination'] = original_destinations[1]

    presplit_formated_destinations = format_destinations(event_body)
    formated_destinations = presplit_formated_destinations.split("|")
    parsed_destinations['formated_start_destination'] = formated_destinations[0]
    parsed_destinations['formated_end_destination'] = formated_destinations[1]


def build_gmaps_url(parsed_destinations):
    url = gmaps_url_base+'origins='+parsed_destinations['start_destination']+'&destinations='+parsed_destinations['end_destination']+'&mode=walking'+'&units=imperial'+'&key='+gmaps_api_token
    print(url)
    return url

def get_gmaps_results(url):
    results = urllib.request.urlopen(url).read()
    return results

def lambda_handler(event, context):
    print("Received event: " + str(event))
    build_parsed_destinations(event['Body'])
    url = build_gmaps_url(parsed_destinations)
    encoded_results = get_gmaps_results(url)

    decoded_results = json.loads(encoded_results.decode('utf-8'))
    print("Results: " + str(decoded_results))

    return '<?xml version=\"1.0\" encoding=\"UTF-8\"?>'\
          '<Response><Message>From: '+ str(decoded_results['destination_addresses'][0]) + ' To: ' + str(decoded_results['origin_addresses'][0]) +' will take about ' + str(decoded_results['rows'][0]['elements'][0]['duration']['text']) +' to get their on foot!'+ '</Message></Response>'
