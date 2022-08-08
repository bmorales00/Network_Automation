##############################################################

## Telnet Example 1

##############################################################
import telnetlib
import time

host = '10.1.1.10' #IP address of the router
port = '23' #Default port for Telnet
user = 'csn' #Username
password = 'cisco' #Non Hardcoded Password

#Telnetlib only works with byte's
tn = telnetlib.Telnet(host)  #Telnet method that connect through the host IP
tn.read_until(b'Username: ') #read_until is a method that will match the telnet ouput and read until a given string
tn.write(user.encode() + b'\n') #Write method will encode the string we are trying to transmit in type byte's
tn.read_until(b'Password: ') #read_until is a method that will match the telnet ouput and read until a given string
tn.write(password.encode() + b'\n') #Write method will encode the string we are trying to transmit in type byte's

tn.write(b'enable\n')#
tn.write(b'cisco\n') #this is to enable the password

tn.write(b'terminal length 0\n') #When executing a command in Cisco, this command will allow to display output without
#pausing.
#tn.write(b'sh running-config\n')
tn.write(b'show ip interface brief\n') #Show the interface of the IP that are up
tn.write(b'exit\n')

"""
"""
output = tn.read_all() #of byte type
print(type(output))
print(output)
"""
"""
output = tn.read_all().decode() #Will decode the byte's to string type be able to be read on Python
print(type(output))
print(output)

##############################################################

## Telnet Example 2 using getpass

##############################################################

import telnetlib

import getpass


host = '10.1.1.10' #IP address of the router
port = '23' #Default port for Telnet
user = 'csn' #Username
#password = 'cisco' #Non Hardcoded Password
password = getpass.getpass() #Used to avoid revealing password through the script

#Telnetlib only works with byte's
tn = telnetlib.Telnet(host)  #Telnet method that connect through the host IP
tn.read_until(b'Username: ') #read_until is a method that will match the telnet ouput and read until a given string
tn.write(user.encode() + b'\n') #Write method will encode the string we are trying to transmit in type byte's
tn.read_until(b'Password: ') #read_until is a method that will match the telnet ouput and read until a given string
tn.write(password.encode() + b'\n') #Write method will encode the string we are trying to transmit in type byte's

tn.write(b'enable\n')#
tn.write(b'cisco\n') #this is to enable the password

tn.write(b'terminal length 0\n') #When executing a command in Cisco, this command will allow to display output without
#pausing.
tn.write(b'sh running-config\n')
tn.write(b'show ip interface brief\n') #Show the interface of the IP that are up
tn.write(b'exit\n')

output = tn.read_all().decode() #Will decode the byte's to string type be able to be read on Python
print(type(output))
print(output)


import telnetlib

host = '10.1.1.10'
port = '23'
user = 'csn'
password = 'cisco'

tn = telnetlib.Telnet(host)
tn.read_until(b'Username: ')
tn.write(user.encode() + b'\n')
tn.read_until(b'Password: ')
tn.write(password.encode() + b'\n')

tn.write(b'enable\n')
tn.write(b'cisco\n')
tn.write(b'sh running-config\n')
tn.write(b'show ip interface brief\n')
tn.write(b'exit\n')

output = tn.read_all().decode()
print(type(output))
print(output)
