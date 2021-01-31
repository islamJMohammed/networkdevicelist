from helper import *
import pytest

file_name = 'NetworkDevice.csv'
count = 5
devices_list =read_file(file_name)
#for device in devices_list:
   # print (device.device_type,device.pid,device.name,device.ip_address,device.user_name,device.password,device.snmp_read_community)
#print (len(devices_list))
def test_device_count():
   assert len(devices_list)==count