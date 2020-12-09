#!/usr/bin/env python3

import sys
import datetime
import numpy as np

def new_vessel(AIS_line, vessel_list, datai):
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

    ais['length'] = AIS_line[12]
    ais['width'] = AIS_line[13]
    ais['draft'] = AIS_line[14]
    ais['cargo'] = AIS_line[15]
    ais['tclass'] = AIS_line[16]

    vessel_list.append(ais)
    datai[int(ais['mmsi'])] = len(vessel_list)-1
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

def extract_ais_data(filename, hour, data, datai):
    f = open(filename, 'r')
    # MMSI,BaseDateTime,LAT,LON,SOG,COG,Heading,VesselName,IMO,
    # CallSign,VesselType,Status,Length,Width,Draft,Cargo,TranscieverClass

    ais = {}
    ais['mmsi'] = '0'
    data.append(ais)

    text = f.readline()
    for line in f.readlines():
        record = line.split(',')

        date_time_obj = datetime.datetime.strptime(record[1], '%Y-%m-%dT%H:%M:%S')
        if hour == date_time_obj.hour:
            mmsi = int(record[0])

            if int(data[datai[mmsi]]['mmsi']) == mmsi and mmsi != 0:
                update_vessel(record, data, datai[mmsi])
            else:
                new_vessel(record, data, datai)

    f.close()

    return data


if __name__ == "__main__":
    if len(sys.argv) > 1:
        filename = sys.argv[1]
        if len(sys.argv) == 3:
            hour = int(sys.argv[2])
    else:
        print(f'Usage:\n{sys.argv[0]} AIS_filename hour')
        sys.exit(1)

    datai = np.zeros(1999999999, dtype=np.int32)
    data = []
    extract_ais_data(filename, hour, data, datai)

    print(len(data))

