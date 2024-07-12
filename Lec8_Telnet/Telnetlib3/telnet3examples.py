from Exscript.protocols import Telnet

host = '10.1.1.10'
username = 'csn'
password = 'cisco'

conn = Telnet()
conn.connect(host)

conn.expect('Username: ')
conn.send(username+'\n')

conn.expect('Password: ')
conn.send(password+'\n')

conn.send('enable\n')
conn.send('cisco\n')

commands = ['show interfaces\n']  # Example commands
for command in commands:
    conn.send(command)
    result = conn.response
    print(result)

conn.send('exit\n')
conn.close()