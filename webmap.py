import folium
import pandas

data = pandas.read_csv("worldcities.csv")
lat = data['lat']
lon = data['lng']
city = data['city']
ppl = data['population']


def color_change(ppl):
    if ppl < 50000:
        return 'green'
    else:
        return 'red'


map = folium.Map(location=(25.80, 77.41), zoom_start=10, tiles="Stamen Terrain")

fgc = folium.FeatureGroup(name="PopulationByCity")

for lt, ln, city, popl in zip(lat, lon, city, ppl):
    fgc.add_child(folium.CircleMarker(location=(lt, ln), radius=5, popup="City: "+city+ "\n Population: " +str(popl),
    fill_color=color_change(popl), color='grey', fill=True, fill_opacity=0.7))

fgw = folium.FeatureGroup(name="PopulationWorld")

fgw.add_child(folium.GeoJson(data=open('world.json', 'r', encoding='utf-8-sig').read(),
style_function=lambda x: {'fillColor':'green' if x['properties']['POP2005'] < 10000000
else 'orange' if 10000000 <= x['properties']['POP2005'] < 20000000 else 'red'}))

map.add_child(fgc)
map.add_child(fgw)
map.add_child(folium.LayerControl())

map.save("WorldMap.html")
