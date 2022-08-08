import paramiko #paramiko package
import time  #time module will allow for a delay in the printing of the commands


ssh_client = paramiko.SSHClient() #assign a ssh client using a variable, this returns an object of ssh client
#performs ssh operations

print(type(ssh_client)) #Display the ssh client type

ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
# ^ the ssh client identifies server using a fingerprint and then saves it in a file name called known host
# ^ is used to bypass without the key, this command will add the key before entering the device

ssh_client.connect(hostname='10.1.1.10', port=22, username='csn', password='cisco', look_for_keys=False,
                   allow_agent=False)
# ip address. port, username, and password can be used as keyword arg
# look for keys will specify to show that there are no public key authentication besides the user and pass
#allow agent allows for key authentication and keeps a private key in the ram memory, but it isnt needed either

remote_connection = ssh_client.invoke_shell() #This will request an interactive shell seession on the channel
print(type(remote_connection))

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
print(type(output))