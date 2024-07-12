class TelnetDevice:
    def __init__(self, IPAddress, userName, passWord, console = None):
        self.IPAddress = IPAddress
        self.userName = userName
        self.passWord = passWord
        self.console = console

    def connect(self):
        import telnetlib
        self.console = telnetlib.Telnet(self.IPAddress)

    def loggingin(self):
        self.console.read_until(b'Username: ')
        self.console.write(self.userName.encode() + b'\n')
        self.console.read_until(b'Password: ')
        self.console.write(self.passWord.encode() + b'\n')


    def executecommand(self, command):
        if(len(command) == 0):
            print("No commands was asked of by the user")
        else:
            self.console.write(command.encode() + b'\n')

    def executemultiple(self, commands):
        for c in commands:
            self.console.write(c.encode() + b'\n')

    def showoutput(self):
        print(self.console.read_all().decode())

    def exit(self):
        self.console.write(b'exit\n')
        print(f"exited out of {self.IPAddress} successfully")