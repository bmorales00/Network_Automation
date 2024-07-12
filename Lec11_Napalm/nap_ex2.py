###############################################################
## Checking Connectivity between devices using Napalm
###############################################################

from napalm import get_network_driver
import json
driver = get_network_driver('ios') #driver object, Specify the type of network driver is being used by napalm
#Napalm will automatically select the set of function based on the driver

opt_args = {'secret': 'cisco' } #Optional Argument for enable password to enter privileged Exec Mode
ios = driver('10.1.1.20', 'csn', 'cisco',optional_args=opt_args)

ios.open() #This opens the connection to communicate with the netwrok device

output = ios.ping('10.1.1.10', count=6)


ping = json.dumps(output,indent=4)
print(ping)


ios.close() #This will close the connection after being used

