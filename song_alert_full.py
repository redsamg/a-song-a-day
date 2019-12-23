import pandas as pd
from pandas.io.json import json_normalize
import spotipy
import spotipy.util as util
import json
import requests
from twilio.rest import Client

# credentials from https://developer.spotify.com/dashboard/applications
client_id = '88490b19c1e244198c16c5cc5c805a50'
secret = '2f533008e057434ba18a9566165a4a25'

# define credentials
token = util.oauth2.SpotifyClientCredentials(client_id=client_id, client_secret=secret)
access_token = token.get_access_token()

# establish connection, define playlist
url = 'https://api.spotify.com/v1/playlists/37i9dQZF1DX5vMTfJy5XKE/tracks' # <- this is where you choose the playlist that you will pull tracks from
headers = {'Authorization': "Bearer {}".format(access_token)}

r = requests.get(url, headers=headers)

# load playlist JSON
loads = json.loads(r.text)

# function to flatten json
def flatten_json(nested_json):
    """
        Flatten json object with nested keys into a single level.
        Args:
            nested_json: A nested json object.
        Returns:
            The flattened json object if successful, None otherwise.
    """
    out = {}

    def flatten(x, name=''):
        if type(x) is dict:
            for a in x:
                flatten(x[a], name + a + '_')
        elif type(x) is list:
            i = 0
            for a in x:
                flatten(a, name + str(i) + '_')
                i += 1
        else:
            out[name[:-1]] = x

    flatten(nested_json)
    return out

r = flatten_json(loads)

# isolate tracks from flattened JSON
track_list = []
counter = 0

for key,value in r.items():
    if "track_external_urls_spotify" in key:
        counter += 1
        track_list.append(value)

# format as dataframe, ensure not truncating string, return a random track 
df = pd.DataFrame(track_list)
pd.set_option("display.max_colwidth", 10000)
random_track = df.sample()
final_track = random_track.to_string(index=False, header=False)

# send SMS via Twilio API service
# Your Account Sid and Auth Token from twilio.com/console
account_sid = 'ACcb7d41a312fb51dfb5cc9f4efa135060'
auth_token = '36d5305ed143c289ec8d514bd2980bf6'
client = Client(account_sid, auth_token)

message = client.messages \
                .create(
                     body="Hey, Sam! Here is the link to your song of the day: " + final_track,
                     from_='+12406502580', # <- enter your Twilio number (https://www.twilio.com/docs/sms/quickstart/python#install-python-and-the-twilio-helper-library)
                     to='+12067185558' # <- enter number(s) of those to whom you wish to text
                 )

print(message.sid)