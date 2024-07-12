from napalm import get_network_driver

# Create a driver object
driver = get_network_driver('ios')

# Define the device parameters
device_ip = '10.1.1.20'
username = 'csn'
password = 'cisco'
optional_args = {'secret': 'cisco'}  # If you have enable secret configured


ios = driver(device_ip,username,password,optional_args=optional_args)

ios.open()
mapper = ios.get_config(full=True)
output = mapper['startup'].splitlines()
output = output[1:]
config = "\n".join(output)
print(config)
with open("config.txt", 'w') as file:
    file.write(config)

ios.close()


# from napalm import get_network_driver
#
# # Create a driver object
# driver = get_network_driver('ios')
#
# # Define the device parameters
# device_ip = '10.1.1.10'
# username = 'csn'
# password = 'cisco'
# optional_args = {'secret': 'cisco'}  # If you have enable secret configured
#
# ios = driver(device_ip, username, password, optional_args=optional_args)
#
# ios.open()
#
# ios.load_replace_candidate(filename="config.txt")
# diff = ios.compare_config()
#
# if diff:
#     print(diff)
#     print(f"Changes will be committed to {device_ip}")
#     ios.commit_config()
# else:
#     print(f"No changes are needed")
#     ios.discard_config()
#
# ios.close()
