"""
____________________________________ Netmiko ______________________________________

* Connecting to a network device using Netmiko
* Sending Commands to multiple network devices using Netmiko
* Sending Commands to a network device using Netmiko from a File
"""

from netmiko import ConnectHandler


ip_addresses = ['10.1.1.10', '10.1.1.20', '10.1.1.30']

for ip in ip_addresses:
    connection_device = {
        'device_type': 'cisco_ios',
        'ip': ip,
        'username': 'csn',
        'password': 'cisco',
        'port': 22,
        'secret': 'cisco'
    }

    connection = ConnectHandler(**connection_device)
    connection.enable()
    output = connection.send_config_from_file("ospf.txt")
    print(output)
    connection.disconnect()
