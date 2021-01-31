import csv
from network_device_class import NetworkDevices

def read_file(file_name):
    list = []
    with open(file_name, 'r') as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
              list.append(NetworkDevices(row[0],row[1],row[2],row[3],row[4],row[5],row[6]))

    return list
