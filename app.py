from helper import *
import pytest
#file_name = 'NetworkDevice.csv'
#count = 6
#devices_list =read_file(file_name)
#for device in devices_list:
   # print (device.device_type,device.pid,device.name,device.ip_address,device.user_name,device.password,device.snmp_read_community)
# print (len(devices_list))


# def test_devices_count():
#    print("\ntesting start")
#    file_name = 'NetworkDevice.csv'
#    print ("\n test_devices_count start testing with file " + file_name)
#    count = 5
#    print ("\n The expected number of devices is " + str(count))
#    devices_list = read_file(file_name)
#    print ("\n The real number of devices is " + str(len(devices_list)))
#
#    assert len(devices_list)==count
#    print ("\n Test Ended")



@pytest.mark.parametrize("file_name",['NetworkDevice.csv'])
def test_devices_count_with_different_file_name(file_name):

   print("\n testing start")
   print ("\n test_devices_count start testing "+ file_name)
   count = 5
   print ("\n The expected number of devices is "+ str(count))
   print ("\n The real number of devices is " + str(len(read_file(file_name))))
   assert len(read_file(file_name))==count
   print ("\n Test Ended")



