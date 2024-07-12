######################################################################

##   Paramiko Examples and Invoke Example 1

######################################################################

import paramiko #paramiko package
import time  #time module will allow for a delay in the printing of the commands


ssh_client = paramiko.SSHClient() #assign a ssh client using a variable, this returns an object of ssh client
#performs ssh operations
print(type(ssh_client)) #Display the ssh client type

#print(f'ESTABLISHING A CONNECTION USING THE FOLLOWING GIVEN IP ADDRESS ....')

ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
# ^ the ssh client identifies server using a fingerprint and then saves it in a file name called known host
# ^ is used to bypass without the key, this command will add the key before entering the device

#ssh_client.connect(hostname='10.1.1.10', port=22, username='csn', password='cisco', look_for_keys=False,allow_agent=False)
# ip address. port, username, and password can be used as keyword arg
# look for keys will specify to show that there are no public key authentication besides the user and pass
#allow agent allows for key authentication and keeps a private key in the ram memory, but it isnt needed either



ciscoR1 = {'hostname': '10.1.1.10', 'port':'22' , 'username' : 'csn', 'password':'cisco'}

ssh_client.connect(**ciscoR1, look_for_keys=False, allow_agent=False) #the **kwarg is used to unpack the created
# -- dictionary to be used as the arguments in the method corresponding to the keywords
#This is another way of establishing a connection
#advatage is that the values of the keys can be used in other parts of the code as such
print(f'The current IP address that is connected is {ciscoR1["hostname"]}')


#print(ssh_client.get_transport().is_active()) #is used to identify if the SSH connection is active



remote_connection = ssh_client.invoke_shell() #This will request an interactive shell seession on the channel
#print(type(remote_connection))

remote_connection.send('terminal length 0\n') #When executing a command in Cisco, this command will allow to display
#output without pausing.
remote_connection.send('show version\n') #\n is mandatory while using paramiko
# #will display info of the OS
# the send function will allow for commands to be sent to the router devices
remote_connection.send('sh ip int brief\n')
time.sleep(1) #a delay of 1 second between each command

output = remote_connection.recv(4096) #recv method takes the number of bytes received at once and returns an object of
# -- type bytes
#print(type(output))

#print(output)
print(output.decode()) # will convert type byte to string object

#ssh_client.close()
if ssh_client.get_transport().is_active() == True:
    ssh_client.close()
#if ssh_client.get_transport().is_active() == True:
    #print(f'CLOSING THE CONNECTION ....')
 #   ssh_client.close() #is used to close the client

"""
######################################################################

##   Paramiko Examples and Invoke Example 2 using getpass

######################################################################
"""
"""
import paramiko
import time
import getpass

ssh_client = paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

print(f'ESTABLISHING A CONNECTION USING THE FOLLOWING GIVEN IP ADDRESS ....')

password = getpass.getpass('Enter a password: ')
ciscoR1 = {'hostname': '10.1.1.10', 'port':'22' , 'username' : 'csn', 'password':password}
print(f'The current IP address that is connected is {ciscoR1["hostname"]}')
ssh_client.connect(**ciscoR1, look_for_keys=False, allow_agent=False)

remote_connection = ssh_client.invoke_shell()
remote_connection.send('terminal length 0\n')
remote_connection.send('show version\n')
remote_connection.send('sh ip int brief\n')
time.sleep(1)

output = remote_connection.recv(4096)

print(output.decode())

if ssh_client.get_transport().is_active() == True:
    print(f'CLOSING THE CONNECTION ....')
    ssh_client.close()

"""


