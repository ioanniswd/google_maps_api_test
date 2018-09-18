# <codecell>
import googlemaps
from datetime import datetime
import json

# <codecell>
with open('cred.json') as f:
    key = json.load(f)['api_key']

gmaps = googlemaps.Client(key=key)


# <codecell>
# Geocoding an address
geocode_result = gmaps.geocode('1600 Amphitheatre Parkway, Mountain View, CA')

# Look up an address with reverse geocoding
reverse_geocode_result = gmaps.reverse_geocode((40.714224, -73.961452))

# Request directions via public transit
now = datetime.now()
directions_result = gmaps.directions("Sydney Town Hall",
                                     "Parramatta, NSW",
                                     mode="transit",
                                     departure_time=now)

# <codecell>
directions_result

# <codecell>
now
