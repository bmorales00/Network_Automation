"""
____________________________________ Paramiko ______________________________________

* Connecting to a network device using Paramiko
* Sending Commands to a network device using Paramiko
* Backing up device configuration using Paramiko and File Handling

"""

import paramiko
import time

client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

_hostname = "10.1.1.10"
_port = 22
_username = "csn"
_password = "cisco"


client.connect(hostname=_hostname, port=_port, username=_username, password=_password)
channel = client.invoke_shell()

channel.send(b'terminal length 0\n')
channel.send(b'enable\n')
channel.send(b'cisco\n')
channel.send(b'sh run\n')
time.sleep(2)

output = channel.recv(4096)

with open(f"{_hostname}-backup.txt", 'w')as file:
    file.write(output.decode())


client.close()

