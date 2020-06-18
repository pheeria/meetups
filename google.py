from datetime import time, datetime as dt, timedelta as td
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import json

# If modifying these scopes, delete the file token.pickle.
SCOPES = [
    'https://www.googleapis.com/auth/calendar',
    'https://www.googleapis.com/auth/calendar.events'
]

def create_service():
    """
    Creates Google Calendar API service.
    """
    creds = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    return build('calendar', 'v3', credentials=creds)

def create_event(event):
    """
    Prepares the event in Google Calendar API format.
    """
    start_time = time.fromisoformat(event["local_time"])
    end_time = (dt.combine(dt.now(), start_time) + td(milliseconds=event["duration"])).time()

    description = f'<a href="{event["link"]}">Link to the Meetup Event</a><br>{event["description"]}'
    return {
        'summary': f'{event["group"]["name"]} — {event["name"]}',
        'location': f'{event["venue"]["name"]}, {event["venue"]["address_1"]}',
        'description': description,
        'start': {
            'dateTime': f'{event["local_date"]}T{start_time}+01:00',
            'timeZone': 'Europe/Berlin',
        },
        'end': {
            'dateTime': f'{event["local_date"]}T{end_time}+01:00',
            'timeZone': 'Europe/Berlin',
        },
    }

def main():
    service = create_service()
    event = create_event({"created":1529409410000,"duration":10800000,"id":"tmqvvpyzqbzb","name":"Berlin.JS","series":{"id":37892995,"template_event_id":0,"description":"Jeden 3. Donnerstag des Monats","start_date":1529553600000,"monthly":{"week_of_month":3,"day_of_week":4,"interval":1}},"date_in_series_pattern":True,"status":"upcoming","time":1576778400000,"local_date":"2019-12-19","local_time":"19:00","updated":1529409410000,"utc_offset":3600000,"waitlist_count":0,"yes_rsvp_count":22,"venue":{"id":17792592,"name":"Berlin Coworking Space - co.up","lat":52.50046157836914,"lon":13.418904304504395,"repinned":False,"address_1":"Adalbertstraße 7 - 8, 10999 Berlin","city":"Berlin","country":"de","localized_country_name":"Deutschland"},"group":{"created":1447920165000,"name":"Berlin.JS","id":19136067,"join_mode":"open","lat":52.52000045776367,"lon":13.380000114440918,"urlname":"Berlin-JS","who":"Berlin JavaScripters","localized_location":"Berlin, Deutschland","state":"","country":"de","region":"de_DE","timezone":"Europe/Berlin"},"link":"https://www.meetup.com/de-DE/Berlin-JS/events/tmqvvpyzqbzb/","description":"<p>About the meetup:</p> <p>Please check berlinjs.org (<a href=\"http://berlinjs.org/\" class=\"linkified\">http://berlinjs.org/</a>) for up-to-date info about the talks we have scheduled for the upcoming event! If there's an open slot, consider making a pull-request to give a talk yourself, or encourage a friend to do the same :)</p> <p>Please get in touch with any of the organizers with any questions you have. We welcome a diverse range of topics that are related in any way to JavaScript and the community around it. New speakers, experienced speakers, and everyone in between. If you have an idea you aren't sure about, just reach out.</p> <p>Drinks can be purchased at 2 euro. There is a small selection of non-alcoholic beverages and beer to choose from.</p> <p>Our Commitment to a Code of Conduct:</p> <p>Our goal is to have an awesome, inclusive and safe community meetup where people meet, hang out together, chat, listen to talks, exchange ideas and make new friends. Any harmful or discriminating behavior will not be tolerated and results in the offending person being expelled from the meetup.</p> <p>For details on what kinds of behavior are not tolerated and consequences for violating these rules, we refer to the Berlin Code of Conduct (<a href=\"http://rubyberlin.github.io/code-of-conduct\" class=\"linkified\">http://rubyberlin.github.io/code-of-conduct</a>).</p> <p>Keep in touch:</p> <p>on twitter: @BerlinJS (<a href=\"https://twitter.com/berlinjs\" class=\"linkified\">https://twitter.com/berlinjs</a>)</p> <p>on the web: berlinjs.org (<a href=\"http://berlinjs.org/\" class=\"linkified\">http://berlinjs.org/</a>)</p> <p>on foursquare: Berlin.JS (<a href=\"http://4sq.com/1K5KgAT\" class=\"linkified\">http://4sq.com/1K5KgAT</a>)</p> <p>Detailed Directions:</p> <p>co.up is located closest to the Kottbusser Tor U-bahn station (U8 &amp; U1).</p> <p>Please note that there are two entrances to the hof where co.up is located. If one gate is closed, the other should be open.</p> <p>If you're attending for the first time, check out the map below.</p> <p><img src=\"http://photos3.meetupstatic.com/photos/event/6/0/f/8/600_444324824.jpeg\" /></p> <p>About our supporters:</p> <p>We are so grateful to be hosted by the wonderful co.up coworking space (<a href=\"http://co-up.de/\" class=\"linkified\">http://co-up.de/</a>) each month at no cost. Therefore, we ask if you enjoy our meetups, please consider supporting co.up's generosity by helping fund upgrades and renovations with a small donation in the jar near the fridge.</p> <p>If you need a coworking space, consider joining co.up!</p> ","how_to_find_us":"Ring the bell for co.up 3rd floor, then come up to the 3rd floor.","visibility":"public","member_pay_fee":False,"comment_count":0})
    service.events().insert(calendarId='primary', body=event).execute()

if __name__ == '__main__':
    main()