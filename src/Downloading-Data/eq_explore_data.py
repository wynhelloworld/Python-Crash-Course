from pathlib import Path
import json

path = Path('./eq_data/all_eq_20231115-20231116.geojson')
contents = path.read_text()
all_eq_data = json.loads(contents)

path = Path('eq_data/readable_eq_data.geojson')
readable_eq_data = json.dumps(all_eq_data, indent=4)
path.write_text(readable_eq_data)

all_eq_dicts = all_eq_data['features']
mags = []
titles = []
lons = []
lats = []
for eq_dict in all_eq_dicts:
    mag = eq_dict['properties']['mag']
    title = eq_dict['properties']['title']
    lon = eq_dict['geometry']['coordinates'][0]
    lat = eq_dict['geometry']['coordinates'][1]
    mags.append(mag)
    titles.append(title)
    lons.append(lon)
    lats.append(lat)

print(mags[:10])
print(titles[:10])
print(lons[:10])
print(lats[:10])
