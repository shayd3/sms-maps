from twilio.rest import Client
import os
import googlemaps

twilio_account_sid = os.environ['TWILIO_SID']
twilio_auth_token  = os.environ['TWILIO_TOKEN']
gmaps_api_token = os.environ['GMAPS_DISTANCE_API_KEY']

gmaps = googlemaps.Client(key=gmaps_api_token)
twil_client = Client(twilio_account_sid, twilio_auth_token)

def get_destination_result(start_destination, end_destination):
    results = gmaps.distance_matrix(start_destination, end_destination, mode="walking",units="imperial")
    return results

def get_start_destination(gmap_results):
    return gmap_results['origin_addresses'][0]

def get_end_destination(gmap_results):
    return gmap_results['destination_addresses'][0]

def get_trip_duration(gmap_results):
    return gmap_results['rows'][0]['elements'][0]['duration']['text']

def get_gmap_status(gmap_results):
    return gmap_results['status']

def send_text(message):
    sms_message = twil_client.messages.create(
        to="+12159832573",
        from_="+18564315999",
        body=message)

if __name__ == '__main__':
    gmap_results = get_destination_result('517 Stratford Road, Glenolden, PA','1741 Fontain Street, Philadelphia, PA')
    import pdb; pdb.set_trace()
    send_text("From " + get_start_destination(gmap_results) +
             " to " + get_end_destination(gmap_results) +
             " will take you " + get_trip_duration(gmap_results) +
             " to drive there!")
