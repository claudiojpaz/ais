# ais
Command line Parser/Ploter of AIS data

## Requirements (older versions may work)

* python 3.8

## Use

Open a terminal, go to your preferred directory and type (without $)

```
$ git clone https://github.com/claudiojpaz/ais.git
```

or download zip file from [here](https://github.com/claudiojpaz/ais/archive/main.zip)

Go into new directory (`ais` for cloned repository and `ais-main` for decompressed version)

```
$ cd ais
```

## Parser

`parser.py` is a module to extract all data from file (v0.01 extracts just 1 chosen hour)

It need csv file downloaded from [here](https://coast.noaa.gov/htdata/CMSP/AISDataHandler/2020/index.html). For example, for a file named `AIS_2020_01_01.csv` corresponding to January 1st 2020, command line is
```
$ ./parser.py AIS_2020_01_01.csv 16
```
to extract all data corresponding to 4pm

From other file, after being imported, the module can be used with

```python
import parser

filename = 'AIS_2020_01_01.csv'
hour = 16
data = []
parser.extract_ais_data(filename, hour, data)

print(data[0])
```

Showed data correspond to the first vessel saved in the file.

`extract_ais_data` open _filename_, extract data corresponding to time _hour_ and append to _data_ (a python list) all the vessels.
Each element of the list is a vessel saved in form of a python dictionary.

Each dictionary have 13 keys, _mmsi_, _dt_, _geo_, _name_, _imo_, callsign_, type_, _status_, _length_, _width_, _draft_, _cargo_ and _tclass_.

All keys except _dt_, _geo_ and _status_ are fixed.

Values of _dt_, _geo_ and _status_ are python lists.
Moreover, _geo_ is a list of dictionaries with keys _lat_, _lon_, _sog_, _cog_ and _heading_

So, to print the name and coordinates of the first vessel in the list

```python
name = data[0]['name']
coordinates = data[0]['geo']
latitude = coordinates[-1]['lat']
longitude = coordinates[-1]['lon']

print(f'Vessel name: {name}')
print(f'Latitude: {latitude}')
print(f'longitude: {longitude}')
```

