#############################################################

## Refactoring Paramiko into a module Example 1

##############################################################
import paramiko
import time

def connect(server_ip,server_port, User, PassW):
    ssh_client = paramiko.SSHClient()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    print(f'Currently Connecting to: {server_ip}"')
    ssh_client.connect(hostname=server_ip, port= server_port , username=User , password=PassW,
                       look_for_keys=False,allow_agent=False)
    return ssh_client

def openshell(ssh_client):
    client = ssh_client.invoke_shell()

    return client

def send_command(client, command, timeout=1 ):
    print(f'Sending command: {command}')
    client.send(command + '\n')
    time.sleep(timeout)

def result(client, n =10000):
    output = client.recv(n)
    return output.decode()

def close(ssh_client):
    if ssh_client.get_transport().is_active() == True:
        ssh_client.close()




"""
shell = connect('10.1.1.10', '22', 'csn', 'cisco')
client = openshell(shell)


send_command(client, 'enable')
send_command(client, 'cisco')
send_command(client, 'terminal length 0')
send_command(client, 'sh version')
send_command(client, 'sh ip int brief')

output = result(client)
print(output)

"""

#############################################################

## Refactoring Paramiko into a module Example 2

##############################################################
"""

ciscoR1 = {'server_ip': '10.1.1.10', 'server_port':'22' , 'User' : 'csn', 'PassW':'cisco'}
ciscoR2 = {'server_ip': '10.1.1.20', 'server_port':'22' , 'User' : 'csn', 'PassW':'cisco'}
ciscoR3 = {'server_ip': '10.1.1.30', 'server_port':'22' , 'User' : 'csn', 'PassW':'cisco'}

routers = [ciscoR1,ciscoR2,ciscoR3]

for ipadd in routers:
    shell = connect(**ipadd)
    client = openshell(shell)

    send_command(client, 'enable')
    send_command(client, 'cisco')
    send_command(client, 'terminal length 0')
    send_command(client, 'sh version')
    send_command(client, 'sh ip int brief')

    output = result(client)
    print(output)
"""

