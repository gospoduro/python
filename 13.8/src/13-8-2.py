#Test data to find place_id: Obninsk Technical University of Nuclear Power Engineering Russia
import urllib.request, urllib.parse, urllib.error
import json
# Note that Google is increasingly requiring keys
# for this API
api_key = False
# If you have a Google Places API key, enter it here
# api_key = 'AIzaSy___IDByT70'
if api_key is False:
    serviceurl = "http://py4e-data.dr-chuck.net/geojson?"
else :
    serviceurl = "https://maps.googleapis.com/maps/api/place/textsearch/json?"
#
while True:
    address = input('Enter location: ')
    if len(address) < 1: break

    url = serviceurl + urllib.parse.urlencode(
        {'address': address})

    print('Retrieving', url)
    uh = urllib.request.urlopen(url)
    data = uh.read().decode()
    print('Retrieved', len(data), 'characters')

    try:
        js = json.loads(data)
    except:
        js = None

    if not js or 'status' not in js or js['status'] != 'OK':
        print('==== Failure To Retrieve ====')
        print(data)
        continue
    
    #print(json.dumps(js, indent=4))
    lat = js["results"][0]["geometry"]["location"]["lat"]
    lng = js["results"][0]["geometry"]["location"]["lng"]
    #print('lat', lat, 'lng', lng)
    location = js['results'][0]['formatted_address']
    place_id = js["results"][0]["place_id"]
    #print(location)
    print('Place id', place_id)
