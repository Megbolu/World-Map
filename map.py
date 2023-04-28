import folium
import pandas

data = pandas.read_csv("Volcanoes.txt")
lat = list(data["LAT"])
lon = list(data["LON"])
elev = list(data["ELEV"])

def color_producer(elevation):
    if elevation < 1000:
        return 'blue'
    elif 1000<= elevation < 3000:
        return 'green'
    else:
        return 'orange'
map = folium.Map(location=[38.58, -99.09], zoom_start=6, tiles="http://{s}.tiles.mapbox.com/v4/wtgeographer.2fb7fc73/{z}/{x}/{y}.png?access_token=YOUR_API_KEY",attr='XXX Mapbox Attribution')

fg = folium.FeatureGroup(name="My Map")

for lt, ln, el in zip(lat, lon, elev):
    fg.add_child(folium.Marker(location=[lt, ln], popup=str(el)+" m", icon=folium.Icon(color=color_producer(el))))

fg.add_child(folium.GeoJson(data=(open('World.json', 'r', encoding='utf-8-sig').read())))
map.add_child(fg)
map.save("Map1.hmtl")
