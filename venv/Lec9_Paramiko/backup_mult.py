#############################################################

## Using the Paramiko Module to backup multiple configurations

##############################################################



import myParamiko

ciscoR1 = {'server_ip': '10.1.1.10', 'server_port':'22' , 'User' : 'csn', 'PassW':'cisco'}
ciscoR2 = {'server_ip': '10.1.1.20', 'server_port':'22' , 'User' : 'csn', 'PassW':'cisco'}
ciscoR3 = {'server_ip': '10.1.1.30', 'server_port':'22' , 'User' : 'csn', 'PassW':'cisco'}
ciscorouters = [ciscoR1, ciscoR2,ciscoR3]

for routers in ciscorouters:
    shell = myParamiko.connect(**routers)
    client = myParamiko.openshell(shell)

    myParamiko.send_command(client, 'enable')
    myParamiko.send_command(client, 'cisco')
    myParamiko.send_command(client, 'terminal length 0 ')
    myParamiko.send_command(client, 'show run')

    output = myParamiko.result(client)
    output_list = output.splitlines()
    output_list = output_list[11:-2]
    new_output = '\n'.join(output_list)
    print(new_output)

    file_name = f'{routers["server_ip"]}.txt'
    with open(file_name, 'w')as file:
        file.write(new_output)

    myParamiko.close(client)