#import telnetlib


class NetworkDevice:
    def __init__(self, ipAdd, userName, passWord, connection=None):
        self.ipAdd = ipAdd
        self.userName = userName
        self.passWord = passWord
        self.connection = connection

    def Connect(self):
        import telnetlib
        self.connection = telnetlib.Telnet(self.ipAdd)

    def Let_me_get_in(self):
        self.connection.read_until(b'Username: ')
        self.connection.write(self.userName.encode() + b'\n')
        self.connection.read_until(b'Password: ')
        self.connection.write(self.passWord.encode() + b'\n')

    def Execution(self, command):
        self.connection.write(command.encode() + b'\n')

    def Output(self):
        outPut = self.connection.read_all().decode()
        return outPut



router1 = NetworkDevice(ipAdd='10.1.1.10', userName='csn', passWord='cisco')
router1.Connect()
router1.Let_me_get_in()
router1.Execution('enable')
router1.Execution('cisco')
router1.Execution('terminal length 0')
router1.Execution('show ip interface brief')
router1.Execution('exit')

result = router1.Output()
print(result)

router2 = NetworkDevice(ipAdd='10.1.1.20', userName='csn', passWord='cisco')
router2.Connect()
router2.Let_me_get_in()
router2.Execution('enable')
router2.Execution('cisco')
router2.Execution('terminal length 0')
router2.Execution('show ip interface brief')
router2.Execution('exit')

result = router2.Output()
print(result)

router3 = NetworkDevice(ipAdd='10.1.1.30', userName='csn', passWord='cisco')
router3.Connect()
router3.Let_me_get_in()
router3.Execution('enable')
router3.Execution('cisco')
router3.Execution('terminal length 0')
router3.Execution('show ip interface brief')
router3.Execution('exit')

result = router3.Output()
print(result)

