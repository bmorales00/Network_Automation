from netmiko import ConnectHandler

connection_device = {
    'device_type': 'cisco_ios',
    'ip': '10.1.1.1',
    'username': 'class',
    'password': 'csn',
    'port': 22,
    'secret': 'csn',
    'verbose': True
    }

connection = ConnectHandler(**connection_device)

connection.enable()

commands = ['int loopback 1',
            'ip address 7.7.7.7 255.255.255.255',
            'exit',
            'username user4 secret were123'
            ]
# these commands are executed in order
output = connection.send_config_set(commands)
# this allows for the execution of the set list of the commands
print(output)

output = connection.send_command_expect('sh run')
# with '.send_command_expect' it will try to read all of the data until it encounters the router prompt in the output.
# perfect for commands with large outputs like 'show run'

print(output)

connection.disconnect()

