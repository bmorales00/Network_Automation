#############################################################

## Using the Paramiko Module in a seperate script

##############################################################
"""
import myParamiko

ciscoR1 = {'server_ip': '10.1.1.10', 'server_port':'22' , 'User' : 'csn', 'PassW':'cisco'}
shell = myParamiko.connect(**ciscoR1)
client = myParamiko.openshell(shell)

myParamiko.send_command(client, 'enable')
myParamiko.send_command(client, 'cisco')
myParamiko.send_command(client, 'terminal length 0 ')
myParamiko.send_command(client, 'show run')

output = myParamiko.result(client)
print(output)

myParamiko.close(client)
"""

#############################################################

## Using the Paramiko Module to backup configuration

##############################################################

import myParamiko

ciscoR1 = {'server_ip': '10.1.1.10', 'server_port':'22' , 'User' : 'csn', 'PassW':'cisco'}
shell = myParamiko.connect(**ciscoR1)
client = myParamiko.openshell(shell)

myParamiko.send_command(client, 'enable')
myParamiko.send_command(client, 'cisco')
myParamiko.send_command(client, 'terminal length 0 ')
myParamiko.send_command(client, 'show run')

output = myParamiko.result(client)
output_list = output.splitlines()
output_list = output_list[11:-2]
new_output = '\n'.join(output_list)
print(new_output)

with open('router1-backup.txt', 'w')as file:
    file.write(new_output)

myParamiko.close(client)
