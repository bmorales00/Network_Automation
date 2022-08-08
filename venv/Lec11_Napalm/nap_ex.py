###############################################################
## Connecting To a Device using Napalm
###############################################################
"""
from napalm import get_network_driver

driver = get_network_driver('ios') #driver object, Specify the type of network driver is being used by napalm
#Napalm will automatically select the set of function based on the driver


#opt_args = {'secret': 'cisco' } #Optional Argument for enable password to enter privileged Exec Mode
#ios = driver('10.1.1.10', 'csn', 'cisco',optional_args=opt_args)
secret_pass = {'secret': 'cisco'}
ios = driver('10.1.1.10', 'csn', 'cisco', optional_args=secret_pass)

ios.open()



ios.close()
"""


"""
ios.open() #This opens the connection to communicate with the netwrok device

#print(help(driver))
#print(type(driver))

print(dir(ios)) #Display the attributes associated with IOS




ios.close() #This will close the connection after being used
"""


###############################################################
## Displaying information using Napalm
###############################################################
"""
from napalm import get_network_driver
import json

driver = get_network_driver('ios') #driver object, Specify the type of network driver is being used by napalm
#Napalm will automatically select the set of function based on the driver


opt_args = {'secret': 'cisco' } #Optional Argument for enable password to enter privileged Exec Mode
ios = driver('10.1.1.10', 'csn', 'cisco',optional_args=opt_args)


ios.open() #This opens the connection to communicate with the netwrok device


output = ios.get_arp_table() #Returns a list of dictionaries for each entry of the arp table
#print(output)


result = json.dumps(output , indent=4) #Converts Python Object to a JSON String
print(result)


with open('arp.txt', 'w') as file:
    file.write(result)

ios.close() #This will close the connection after being used
"""

###############################################################
## Retrieving information using Napalm
###############################################################

from napalm import  get_network_driver
import json
driver = get_network_driver('ios') #driver object, Specify the type of network driver is being used by napalm
#Napalm will automatically select the set of function based on the driver


opt_args = {'secret': 'cisco' } #Optional Argument for enable password to enter privileged Exec Mode
ios = driver('10.1.1.30', 'csn', 'cisco',optional_args=opt_args)


ios.open() #This opens the connection to communicate with the netwrok device


#output= ios.get_facts() #returns information based on the device
#print(output)
#result = json.dumps(output, indent=4)
#print(result)

#output = ios.get_interfaces() #Displays information about each device interface
#print(output)
#result =json.dumps(output,indent=4)
#print(result)

#output = ios.get_interfaces_counters() #Displays information about each device interface based on packets transmitted
#print(output)
#result =json.dumps(output,indent=4)
#print(result)

#output = ios.get_interfaces_ip() #Displays information about each device's IP Address
#result =json.dumps(output,indent=4)
#print(result)

#output = ios.get_users() #Displays user information
#result =json.dumps(output,indent=4)
#print(result)

ios.close() #This will close the connection after being used


from napalm import  get_network_driver
import json
driver = get_network_driver('ios')

opt_args = {'secret': 'cisco' }
ios = driver('10.1.1.30', 'csn', 'cisco',optional_args=opt_args)

ios.open()

output = ios.get_interfaces()
result =json.dumps(output,indent=4)
print(result)


ios.close()

"""
from napalm import get_network_driver
import json

driver = get_network_driver('ios') #driver object, Specify the type of network driver is being used by napalm
#Napalm will automatically select the set of function based on the driver


#opt_args = {'secret': 'cisco' } #Optional Argument for enable password to enter privileged Exec Mode
#ios = driver('10.1.1.10', 'csn', 'cisco',optional_args=opt_args)

secret_pass = {'secret': 'cisco'}
ios = driver(hostname='10.1.1.10', username='csn', password='cisco', timeout=10,optional_args=secret_pass)
ios.open()


print(ios.get_interfaces_ip())

ios.close()

"""