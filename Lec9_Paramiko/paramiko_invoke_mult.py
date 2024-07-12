######################################################################

##   Paramiko Examples and Invoke using multiple devices Example 1

######################################################################
import paramiko
import time

ssh_client = paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

ciscoR1 = {'hostname': '10.1.1.10', 'port':'22' , 'username' : 'csn', 'password':'cisco'}
ciscoR2 = {'hostname': '10.1.1.20', 'port':'22' , 'username' : 'csn', 'password':'cisco'}
ciscoR3 = {'hostname': '10.1.1.30', 'port':'22' , 'username' : 'csn', 'password':'cisco'}

routerList = [ciscoR1,ciscoR2,ciscoR3]

for router in routerList:
    print(f'Currently Connecting to: {router["hostname"]}')
    ssh_client.connect(**router, look_for_keys=False, allow_agent=False)
    remote_connection = ssh_client.invoke_shell()

    remote_connection.send('enable\n')
    remote_connection.send('cisco\n')
    remote_connection.send('configure terminal\n')
    remote_connection.send('router ospf 1\n')
    remote_connection.send('net 0.0.0.0 0.0.0.0 area 0\n')
    remote_connection.send('end\n')
    remote_connection.send('terminal length 0\n')
    remote_connection.send('sh ip protocols\n')
    time.sleep(1)

    output = remote_connection.recv(4096)

    print(output.decode())

    if ssh_client.get_transport().is_active() == True:
        ssh_client.close()