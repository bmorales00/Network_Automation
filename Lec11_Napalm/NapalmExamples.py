"""
____________________________________ Napalm ______________________________________

* Connecting to a network device using Napalm
* Setting up SCP in a network device
* Sending Commands with SCP through a network device using Napalm

"""

from napalm import get_network_driver

driver = get_network_driver('ios')

device_ip = '10.1.1.10'
_username = 'csn'
_password = 'cisco'
_optional_args = {'secret': 'cisco'}

ios = driver(hostname=device_ip, username=_username, password=_password, optional_args=_optional_args)
ios.open()

partial = ios.get_config(full=True)
full = partial['startup'].splitlines()
full= full[1:]
output = "\n".join(full)
print(output)


ios.close()

