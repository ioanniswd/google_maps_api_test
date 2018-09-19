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


# <codecell>
res = gmaps.distance_matrix(origins='Washington,DC', destinations='New+York+City,NY')

# <codecell>
res


# <codecell>
res = gmaps.distance_matrix(
    origins='Thessaloniki, Greece',
    destinations='Athens, Greece',
    mode='transit')
res


# <codecell>
thess = gmaps.geocode('Thessaloniki, Greece')

# <codecell>
print(json.dumps(thess, indent=2))

# <codecell>
thess[0]['geometry']['location']

# <codecell>
res = gmaps.distance_matrix(
    origins='40.6400629,22.9444191',
    destinations='Athens, Greece',
    mode='transit')
res

# <codecell>
res = gmaps.places('Bar', 'Bar')

# <codecell>
res

# <codecell>
location = (40.6400629, 22.9444191)

# <codecell>
res = gmaps.places_nearby(
    location=location,
    # keyword='foo',
    name='school',
    # rank_by='distance',
    radius=1000,
    type='school'
)

# <codecell>
print(json.dumps(res, indent=2, ensure_ascii=False))


# <codecell>
len(res['results'])

# <codecell>
for loc in res['results']:
    print(loc['name'])


# <codecell>
geocode_result = gmaps.geocode('Anaximenous 5, Pylaia, Thessaloniki, Greece')

# <codecell>
geocode_result

# <codecell>
my_loc = geocode_result[0]['geometry']['location']
my_loc

# <codecell>
res = gmaps.places_nearby(
    location=my_loc,
    # keyword='foo',
    name='supermarket',
    # rank_by='distance',
    radius=300,
    type='supermarket'
)

# <codecell>
len(res['results'])

# <codecell>
res

# <codecell>
[x['name'] for x in res['results']]

# <codecell>
