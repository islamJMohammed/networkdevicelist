from helper import *

file_name = 'NetworkDevice.csv'

devices_list =read_file(file_name)

for device in devices_list:
    print (device.device_type,device.pid,device.name,device.ip_address,device.user_name,device.password,device.snmp_read_community)

