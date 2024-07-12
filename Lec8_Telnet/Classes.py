##############################################################

## Telnet Class Example:

##############################################################

class Device: #These devices can go as far as meaning switches and routers
    def __init__(self, ipadd, userName, passWord, connection=None): #arug of constructor (self) is reference to object that calls this method
        self.ipadd = ipadd
        self.userName = userName
        self.passWord = passWord
        self.connection = connection

    def connect(self):
        import telnetlib
        self.connection = telnetlib.Telnet(self.ipadd)

    def authentication(self):
        self.connection.read_until(b'Username: ')
        self.connection.write(self.userName.encode() + b'\n')
        self.connection.read_until(b'Password: ')
        self.connection.write(self.passWord.encode() + b'\n')

    def execution(self, command):
        self.connection.write(command.encode() + b'\n')

    def showcomm(self):
        outPut = self.connection.read_all().decode()
        return outPut
"""
router1 = Device(ipadd= '10.1.1.10', userName='csn', passWord='csn140')
router1.connect()
router1.authentication()
router1.execution('enable')
router1.execution('cisco')
router1.execution('terminal length 0') #To set the number of lines displayed to bypass the pasue session that show ip does
router1.execution('configure terminal')
router1.execution('interface loopback 0')
router1.execution('ip address 1.1.1.1 255.255.255.255') #This allows for a traffic bound for a single host
router1.execution('exit')
router1.execution('router ospf 1') #enter ospf using router1
router1.execution('network 0.0.0.0 0.0.0.0 area 0') #specifying the network will send in the routing updates, best possible path selection
router1.execution('end')
router1.execution('show ip protocols')
router1.execution('exit')

outPut = router1.showcomm()

print(outPut)
"""
##############################################################

## Telnet File Example:

##############################################################

with open('devices', 'r') as file:
    device = file.read().splitlines()
    print(device)
    
ip_addresses = list()
print(ip_addresses)

for item in device:
    temp = item.split(':')
    ip_addresses.append(list(temp))
    print(ip_addresses)

    
for element in ip_addresses:

    router1 = Device(element[0], 'csn', 'cisco')
    router1.connect()
    router1.authentication()
    router1.execution('enable')
    router1.execution('cisco')
    router1.execution('terminal length 0') #To set the number of lines displayed to bypass the pasue session that show ip does
    router1.execution('configure terminal')
    router1.execution('interface loopback 0')
    router1.execution('ip address ' + str(element[0]) + ' 255.255.255.255') #This allows for a traffic bound for a single host
    router1.execution('exit')
    router1.execution('router ospf 1') #enter ospf using router1
    router1.execution('network 0.0.0.0 0.0.0.0 area 0') #specifying the network will send in the routing updates, best possible path selection
    router1.execution('end')
    router1.execution('show ip protocols')
    router1.execution('exit')

    outPut = router1.showcomm()
    print(outPut)


##############################################################

## The file:

##############################################################
"""
with open('devices', 'r') as file:
    device = file.read().splitlines()
    print(device)

ip_addresses = list()
print(ip_addresses)

for item in device:
    temp = item.split(':')
    ip_addresses.append(list(temp))
    print(ip_addresses)
"""