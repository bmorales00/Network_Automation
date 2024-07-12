from netmiko import Netmiko
from netmiko import ConnectHandler


connection_device = {
    'device_type': 'cisco_ios',
    'ip': '10.1.1.30',
    'username': 'csn',
    'password': 'class',
    'port':22,
    'secret':'class',
    'verbose':True
}

connection = ConnectHandler(**connection_device)

print('Entering enable mode ...')
connection.enable()



command = ['exit',
           'sh ip protocols',
           'sh run'
]

output = connection.send_config_set(command)
#print(output)

#print(help(connection))
prompt = connection.find_prompt()
hostname = prompt[:-1]

#print(hostname)
backup_file = (f'{hostname}-backup.txt')
with open(backup_file, 'w') as backup:
    backup.write(output)
    print(f'Backup of {hostname} Completed!!!!!!!!')


print("\nDisconnecting from the device...")
connection.disconnect()




"""
routers = ['10.1.1.10', '10.1.1.20', '10.1.1.30']

device_list = []

for ip in routers:
    connection_device = {
        'device_type': 'cisco_ios',
        'ip': ip,
        'username': 'csn',
        'password': 'class',
        'port':22,
        'secret':'class',
        'verbose':True
    }
    device_list.append(connection_device)


#print(device_list)

for device in device_list:

    print('Connecting to' + device['ip'])
    connection = ConnectHandler(**device)

    print('Entering the Enable Mode...')
    connection.enable()

    file = input('Enter the file that will be transmitted to ' + device['ip']+':')
    print('Running Commands from File ' + file + ' to device: '+ device['ip'])
    output = connection.send_config_from_file(file)
    print(output)

    print("\nDisconnecting from the device...")
    connection.disconnect()
    print("\n")
"""



"""
connection_device = {
    'device_type': 'cisco_ios',
    'ip': '10.1.1.10',
    'username': 'csn',
    'password': 'class',
    'port':22,
    'secret':'class',
    'verbose':True
}

connection = ConnectHandler(**connection_device)

print('Entering the Enable Mode...')
connection.enable()

print('Sending Commands from the File ospf.txt ...')

output = connection.send_config_from_file('ospf.txt')
print(output)

print("\nDisconnecting from the device...")
connection.disconnect()
"""



from netmiko import Netmiko
from netmiko import ConnectHandler

connection_device = {
    'device_type': 'cisco_ios',
    'ip': '10.1.1.10',
    'username': 'csn',
    'password': 'class',
    'port':23,
    'secret':'class',
    'verbose':True
}

connection = ConnectHandler(**connection_device)

print('Entering the Enable Mode...')
connection.enable()

commands = {'int loopback 0',
            'ip address 1.1.1.1 255.255.255.255',
            'exit',
            'username user100 secret user100'
            }

output = connection.send_command(commands)

print(output)

print("\nDisconnecting from the device...")
connection.disconnect()



"""
connection_device = {
    'device_type': 'cisco_ios',
    'ip': '10.1.1.10',
    'username': 'csn',
    'password': 'class',
    'port':22,
    'secret':'class',
    'verbose':True
}

connection = ConnectHandler(**connection_device)

output = connection.send_command('sh ip int brief')
print(output)

print("\nDisconnecting from the device...")
connection.disconnect()
"""


"""
connection = Netmiko(host='10.1.1.10', username='csn', password='class', device_type='cisco_ios')

output = connection.send_command('show ip interface brief')

print(output)

print("\nDisconnecting from the device...")
connection.disconnect()
"""



