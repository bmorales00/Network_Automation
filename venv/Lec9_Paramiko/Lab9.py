"""
import paramiko

ssh_client = paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

#print(f'ESTABLISHING A CONNECTION USING THE FOLLOWING GIVEN IP ADDRESS ....')


ciscoR1 = {'hostname': '10.1.1.10', 'port':'22' , 'username' : 'csn', 'password': 'cisco'}
#print(f'The current IP address that is connected is {ciscoR1["hostname"]}')
ssh_client.connect(**ciscoR1, look_for_keys=False, allow_agent=False)

remote_connection = ssh_client.invoke_shell()

with open('commands.txt', 'r') as file:
    commands = file.read().splitlines()
    print(commands)

for x in commands:
    print(f'Currently Executing Command {x}')
    remote_connection.send(x +'\n')

output = remote_connection.recv(4096)
print(output.decode())
"""

"""

import paramiko
import time


ssh_client = paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())




ciscoR1 = {'hostname': '10.1.1.10', 'port':'22' , 'username' : 'csn', 'password': 'cisco'}
print(f'The current IP address that is connected is {ciscoR1["hostname"]}')
ssh_client.connect(**ciscoR1, look_for_keys=False, allow_agent=False)

remote_connection = ssh_client.invoke_shell()
with open('commands.txt', 'r') as file:
    commands = file.read().splitlines()
    print(commands)
for cmd in commands:
    print(f'Executing {cmd}')
    remote_connection.send(cmd + '\n')
    time.sleep(1)

    output = remote_connection.recv(4096)

    print(output.decode())

"""




import paramiko
import time


ssh_client = paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())




ciscoR1 = {'hostname': '10.1.1.10', 'port':'22' , 'username' : 'csn', 'password': 'cisco'}
ciscoR2 = {'hostname': '10.1.1.20', 'port':'22' , 'username' : 'csn', 'password': 'cisco'}
ciscoR3 = {'hostname': '10.1.1.30', 'port':'22' , 'username' : 'csn', 'password': 'cisco'}

router = [ciscoR1,ciscoR2,ciscoR3]

for netdevice in router:

    print(f'The current IP address that is connected is {netdevice["hostname"]}')
    ssh_client.connect(**netdevice, look_for_keys=False, allow_agent=False)


    remote_connection = ssh_client.invoke_shell()

    with open('commands.txt', 'r') as file:
        commands = file.read().splitlines()
        print(commands)
    for cmd in commands:
        print(f'Executing {cmd}')
        remote_connection.send(cmd + '\n')
        time.sleep(1)

        output = remote_connection.recv(4096)

        print(output.decode())



import paramiko
import time


ssh_client = paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())




ciscoR1 = {'hostname': '10.1.1.10', 'port':'22' , 'username' : 'csn', 'password': 'cisco'}
ciscoR2 = {'hostname': '10.1.1.20', 'port':'22' , 'username' : 'csn', 'password': 'cisco'}
ciscoR3 = {'hostname': '10.1.1.30', 'port':'22' , 'username' : 'csn', 'password': 'cisco'}

router = [ciscoR1,ciscoR2,ciscoR3]

for netdevice in router:

    print(f'The current IP address that is connected is {netdevice["hostname"]}')
    ssh_client.connect(**netdevice, look_for_keys=False, allow_agent=False)


    remote_connection = ssh_client.invoke_shell()

    file_name = input('Please enter the file name you wish to use: ')
    with open(file_name, 'r') as file:
        commands = file.read().splitlines()
        print(commands)
    for cmd in commands:
        print(f'Executing {cmd}')
        remote_connection.send(cmd + '\n')
        time.sleep(1)

        output = remote_connection.recv(4096)

        print(output.decode())















