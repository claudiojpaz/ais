#!/usr/bin/env python3

import parser

filename = 'AIS_2020_06_30.csv'
hour = 16
data = []
parser.extract_ais_data(filename, hour, data)

# print(data[0])

print(f"Vessel name: {data[0]['name']}")
coordinates = data[0]['geo']
latitude = coordinates[-1]['lat']
longitude = coordinates[-1]['lon']
print(f'Latitude: {latitude}')
print(f'longitude: {longitude}')

