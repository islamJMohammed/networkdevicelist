class NetworkDevices:
  def __init__(self,device_type,pid,name,ip_address,user_name,password,snmp_read_community):
      self.device_type=device_type
      self.pid=pid
      self.name=name
      self.ip_address=ip_address
      self.user_name=user_name
      self.password=password
      self.snmp_read_community=snmp_read_community