"""
import paramiko
import time

host = paramiko.SSHClient()

host.set_missing_host_key_policy(paramiko.AutoAddPolicy())

R1 = {'hostname' : '10.1.1.11', 'port' : 22, 'username' : 'Perla', 'password' : 'python'}
R2 = {'hostname' : '10.1.1.22', 'port' : 22, 'username' : 'Perla', 'password' : 'python'}
R3 = {'hostname' : '10.1.1.33', 'port' : 22, 'username' : 'Perla', 'password' : 'python'}

my_routers = [R1, R2, R3]

for router in my_routers:
    print(f'''
        ------------------------------------------
        | Establishing connection with {router["hostname"]} |
        ------------------------------------------''')
    host.connect(**router, look_for_keys= False, allow_agent= False)

    secured_connection = host.invoke_shell()

    filename = ["r1.txt", "r2.txt", "r3.txt"]


    for text in filename:
        with open(text, 'r') as file:
            commands = file.read().splitlines()

            for x in commands:
                secured_connection.send(x + '\n')

                time.sleep(1)

                output = secured_connection.recv(4096)

                print(output.decode())

host.close()
"""

import paramiko
import time

host = paramiko.SSHClient()

host.set_missing_host_key_policy(paramiko.AutoAddPolicy())

R1 = {'hostname' : '10.1.1.11', 'port' : 22, 'username' : 'Perla', 'password' : 'python'}
R2 = {'hostname' : '10.1.1.22', 'port' : 22, 'username' : 'Perla', 'password' : 'python'}
R3 = {'hostname' : '10.1.1.33', 'port' : 22, 'username' : 'Perla', 'password' : 'python'}

my_routers = [R1, R2, R3]

for router in my_routers:
    print(f'''
        ------------------------------------------
        | Establishing connection with {router["hostname"]} |
        ------------------------------------------''')
    host.connect(**router, look_for_keys= False, allow_agent= False)

    secured_connection = host.invoke_shell()

    filename = ["r1.txt", "r2.txt", "r3.txt"]

    if router["hostname"] == '10.1.1.11':
        with open(filename[0], 'r') as file:
            commands = file.read().splitlines()
        for x in commands:
            secured_connection.send(x + '\n')

            time.sleep(1)

            output = secured_connection.recv(4096)

            print(output.decode())

    elif router["hostname"] == '10.1.1.22':
        with open(filename[1], 'r') as file:
            commands = file.read().splitlines()
        for x in commands:
            secured_connection.send(x + '\n')

            time.sleep(1)

            output = secured_connection.recv(4096)

            print(output.decode())
    else:
        with open(filename[2], 'r') as file:
            commands = file.read().splitlines()
        for x in commands:
            secured_connection.send(x + '\n')

            time.sleep(1)

            output = secured_connection.recv(4096)

            print(output.decode())




host.close()