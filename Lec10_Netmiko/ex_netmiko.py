
#***********************************************************EXAMPLE_1.1*****************************************#
from netmiko import Netmiko #The from keyword allows use to pick and choose classes to import from said module

connection1 = Netmiko(host='10.1.1.10', port=22, username='csn', password='cisco', device_type='cisco_ios')

# the connection variable will hold the Netmiko function and its arugments
"""
output = connection.send_command('sh ip int brief')
#just displays one ouput of one command
print(output)
#netmiko strips away the router configuration output as it just displays only the command ouput

connection.disconnect()
"""
#**********************************************************Example_1.2********************************************#

"""
from netmiko import Netmiko
from netmiko import ConnectHandler

connection_device = {
    'device_type':'cisco_ios',
    'ip':'10.1.1.1',
    'username':'class',
    'password':'csn',
    'port':22,
    'secret':'csn',
    'verbose':True
}
#using the connection handler requires a format in terms of a dictionary
#the minimum information needed to ssh is just ip/host, device type, and password

connection = ConnectHandler(**connection_device)
#variable that calls the connectionhandler for the dictionary
output = connection.send_command('sh ip int brief')

#just displays one ouput of one command
print(output)
#netmiko strips away the router configuration output as it just displays only the command ouput

connection.disconnect()

"""
"""

from netmiko import ConnectHandler
#import getpass

connection_device = {
    'device_type': 'cisco_ios',
    'ip': '10.1.1.10',
    'username': 'csn',
    'password': 'cisco',
    'port': 22,
    'secret': 'csn',
    'verbose': True
    }
connection = ConnectHandler(**connection_device)
connection.enable()

commands = ['int loopback 1',
            'ip address 7.7.7.7 255.255.255.255',
            'exit',
            'username user4 secret were123'
            ]
# these commands are executed in order
output = connection.send_config_set(commands)
# this allows for the execution of the set list of the commands
print(output)
output = connection.send_command_expect('sh run')
# with '.send_command_expect' it will try to read all of the data until it encounters the router prompt in the output.

print(output)

connection.disconnect()
"""
