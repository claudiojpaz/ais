#!/usr/bin/env python3

import sys
import datetime

def new_vessel(AIS_line, vessel_list):
    ais = {}
    ais['mmsi'] = AIS_line[0]

    ais['dt'] = []
    ais['dt'].append(AIS_line[1])

    coord = {}
    coord['lat'] = AIS_line[2]
    coord['lon'] = AIS_line[3]
    coord['sog'] = AIS_line[4]
    coord['cog'] = AIS_line[5]
    coord['heading'] = AIS_line[6]

    ais['geo'] = []
    ais['geo'].append(coord)

    ais['name'] = AIS_line[7]
    ais['imo'] = AIS_line[8]
    ais['callsign'] = AIS_line[9]
    ais['type'] = AIS_line[10]

    ais['status'] = []
    ais['status'].append(AIS_line[11])

    vessel_list.append(ais)
    #

def update_vessel(AIS_line, vessel_list, i):
    vessel_list[i]['dt'].append(AIS_line[1])

    coord = {}
    coord['lat'] = AIS_line[2]
    coord['lon'] = AIS_line[3]
    coord['sog'] = AIS_line[4]
    coord['cog'] = AIS_line[5]
    coord['heading'] = AIS_line[6]

    vessel_list[i]['geo'].append(coord)

    vessel_list[i]['status'].append(AIS_line[11])
    #

def extract_ais_data(filename, hour, data):
    f = open(filename, 'r')
    # MMSI,BaseDateTime,LAT,LON,SOG,COG,Heading,VesselName,IMO,
    # CallSign,VesselType,Status,Length,Width,Draft,Cargo,TranscieverClass

    ais = {}
    ais['mmsi'] = ''
    data.append(ais)

    text = f.readline()
    for line in f.readlines():
        record = line.split(',')

        date_time_obj = datetime.datetime.strptime(record[1], '%Y-%m-%dT%H:%M:%S')
        if hour == date_time_obj.hour:
            mmsi = record[0]

            for vessel in data:
                if vessel['mmsi'] == mmsi:
                    update_vessel(record, data, data.index(vessel))
                    break
            else:
                new_vessel(record, data)

    f.close()
    data.pop(0)

    return data


if __name__ == "__main__":
    if len(sys.argv) > 1:
        filename = sys.argv[1]
        if len(sys.argv) == 3:
            hour = int(sys.argv[2])
    else:
        print(f'Usage:\n{sys.argv[0]} AIS_filename hour')
        sys.exit(1)

    data = []
    extract_ais_data(filename, hour, data)

    mmsi = '367783480'
    for vessel in data:
        if vessel['mmsi'] == mmsi:
            print(vessel)
            break

    print(len(data))

