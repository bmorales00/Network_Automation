##############################################################

## Telnet Multiple Devices Example 1

##############################################################



import telnetlib
#import getpass

host_list = ['10.1.1.10','10.1.1.20','10.1.1.30'] # A list to hold all the ip addresses
for host in host_list: #For Loop to iterate each router to run the same commands
    user = 'csn'       #Username
    password = 'cisco' #Non Hardcoded Password
    #password = getpass.getpass()

    tn = telnetlib.Telnet(host)   #telnet command that allows for the telnet protocol among the hosts.
    tn.read_until(b'Username: ')  # telnet command that reads a string
    tn.write(user.encode() + b'\n') #telnet command that allows for input to the socket
    tn.read_until(b'Password: ')
    tn.write(password.encode() + b'\n')

    tn.write(b'enable\n')
    tn.write(b'cisco\n') #this is to enable the password
    tn.write(b'configure terminal\n')
    tn.write(b'ip route 0.0.0.0 0.0.0.0 e0/0 10.1.1.2\n')
    tn.write(b'end\n')
    tn.write(b'sh ip route\n')
    tn.write(b'exit\n')

    res = tn.read_all().decode() #command that allows for everything to be read

    print(res)


##############################################################

## Telnet Multiple Devices Example 2

##############################################################
"""
#In case the user has a different password and username for each device:

import telnetlib
#import getpass

host_list = ['10.1.1.10','10.1.1.20','10.1.1.30'] # A list to hold all the ip addresses
for host in host_list: #For Loop to iterate each router to run the same commands

    if host == '10.1.1.10':

        user = 'csn'       #Username
        password = 'csn140' #Non Hardcoded Password
    #password = getpass.getpass()

        tn = telnetlib.Telnet(host)   #telnet command that allows for the telnet protocol among the hosts.
        tn.read_until(b'Username: ')  # telnet command that reads a string
        tn.write(user.encode() + b'\n') #telnet command that allows for input to the socket
        tn.read_until(b'Password: ')
        tn.write(password.encode() + b'\n')

        tn.write(b'enable\n')
        tn.write(b'cisco\n') #this is to enable the password
        tn.write(b'configure terminal\n')
        tn.write(b'ip route 0.0.0.0 0.0.0.0 e0/0 10.1.1.2\n')
        tn.write(b'end\n')
        tn.write(b'sh ip route\n')
        tn.write(b'exit\n')

        res = tn.read_all().decode() #command that allows for everything to be read

        print(res)
    elif host == '10.1.1.20':
        user = 'csn'  # Username
        password = 'cisco'  # Non Hardcoded Password
        # password = getpass.getpass()

        tn = telnetlib.Telnet(host)  # telnet command that allows for the telnet protocol among the hosts.
        tn.read_until(b'Username: ')  # telnet command that reads a string
        tn.write(user.encode() + b'\n')  # telnet command that allows for input to the socket
        tn.read_until(b'Password: ')
        tn.write(password.encode() + b'\n')

        tn.write(b'enable\n')
        tn.write(b'cisco\n')  # this is to enable the password
        tn.write(b'configure terminal\n')
        tn.write(b'ip route 0.0.0.0 0.0.0.0 e0/0 10.1.1.2\n')
        tn.write(b'end\n')
        tn.write(b'sh ip route\n')
        tn.write(b'exit\n')

        res = tn.read_all().decode()  # command that allows for everything to be read

        print(res)
    elif host == '10.1.1.30':
        user = 'csn'  # Username
        password = 'cisco'  # Non Hardcoded Password
        # password = getpass.getpass()

        tn = telnetlib.Telnet(host)  # telnet command that allows for the telnet protocol among the hosts.
        tn.read_until(b'Username: ')  # telnet command that reads a string
        tn.write(user.encode() + b'\n')  # telnet command that allows for input to the socket
        tn.read_until(b'Password: ')
        tn.write(password.encode() + b'\n')

        tn.write(b'enable\n')
        tn.write(b'cisco\n')  # this is to enable the password
        tn.write(b'configure terminal\n')
        tn.write(b'ip route 0.0.0.0 0.0.0.0 e0/0 10.1.1.2\n')
        tn.write(b'end\n')
        tn.write(b'sh ip route\n')
        tn.write(b'exit\n')

        res = tn.read_all().decode()  # command that allows for everything to be read

        print(res)
    else:
        break
        
"""