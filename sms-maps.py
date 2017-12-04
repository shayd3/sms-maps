from twilio.rest import Client
import os
import googlemaps

twilio_account_sid = os.environ['TWILIO_SID']
twilio_auth_token  = os.environ['TWILIO_TOKEN']
gmaps_api_token = os.environ['GMAPS_DISTANCE_API_KEY']

gmaps = googlemaps.Client(key=gmaps_api_token)
twil_client = Client(twilio_account_sid, twilio_auth_token)

def get_destination_result(start_destination, end_destination):
    results = gmaps.distance_matrix(start_destination, end_destination, mode="driving",units="imperial")
    return results

def send_text(message):
    sms_message = twil_client.messages.create(
        to="+12159832573",
        from_="+18564315999",
        body=message)

if __name__ == '__main__':
    gmap_results = get_destination_result('517 Stratford Road, Glenolden, PA','1741 Fontain Street, Philadelphia, PA')
    send_text("From " + gmap_results['origin_addresses'][0] +
             " to " + gmap_results['destination_addresses'][0] +
             " will take you " + gmap_results['rows'][0]['elements'][0]['duration']['text'] +
             " to drive there!")
