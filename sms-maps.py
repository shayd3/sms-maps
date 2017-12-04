from twilio.rest import Client
import os, googlemaps

twilio_account_sid = os.environ['TWILIO_SID']
twilio_auth_token  = os.environ['TWILIO_TOKEN']
gmaps_api_token = os.environ['GMAPS_DISTANCE_API_KEY']

gmaps = googlemaps.Client(key=gmaps_api_token)
twilClient = Client(twilio_account_sid, twilio_auth_token)

def getDestinationResult(startDestination, endDestination):
    results = gmaps.distance_matrix(startDestination, endDestination, mode="driving",units="imperial")
    return results

def sendText(message):
    textMessage = twilClient.messages.create(
        to="+12159832573",
        from_="+18564315999",
        body=message)

if __name__ == '__main__':
    gmapResults = getDestinationResult('517 Stratford Road, Glenolden, PA','1741 Fontain Street, Philadelphia, PA')
    sendText("From " + gmapResults['origin_addresses'][0] + " to " + gmapResults['destination_addresses'][0] + " will take you " + gmapResults['rows'][0]['elements'][0]['duration']['text'] + " to drive there!")
