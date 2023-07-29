import json

# Explore the structure of the data.
filename = 'data/eq_data_1_day_m1.json'
with open(filename) as f:
    all_eq_data = json.load(f)

all_eq_dicts = all_eq_data['features']

mags, lons, lats = [], [], []
for eq_dict in all_eq_dicts:
    mag = eq_dict['properties']['mag']
    lon = eq_dict['geometry']['coordinates'][0]
    lat = eq_dict['geometry']['coordinates'][1]
    mags.append(mag)
    lons.append(lon)
    lats.append(lat)

# Print first 10 magnitudes, longitudes, latitudes
print(mags[:10])
print(lons[:10])
print(lats[:10])
# [0.96, 1.2, 4.3, 3.6, 2.1, 4, 1.06, 2.3, 4.9, 1.8]
# [-116.7941667, -148.9865, -74.2343, -161.6801, -118.5316667, -144.1283, -116.7433333, -153.7845, 59.3991, -116.2045]
# [33.4863333, 64.6673, -12.1025, 54.2232, 35.3098333, 69.5346, 33.5148333, 59.6106, -30.7399, 37.0572]