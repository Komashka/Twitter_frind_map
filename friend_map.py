import folium
from geopy import ArcGIS
from twitter2 import parser
import pdb

myMap = folium.Map()


def map_formation(twi):
    js = parser(twi)
    fg = folium.FeatureGroup(name="Pointers")

    for line in js['users']:
        try:
            # Decoding an address of location
            geolocator = ArcGIS(timeout=10)
            location = geolocator.geocode(line['location'])
            fg.add_child(
                folium.Marker(location=[location.latitude, location.longitude], popup=line['name'],
                              icon=folium.Icon(color="red")))
        except AttributeError:
            continue

    return fg
