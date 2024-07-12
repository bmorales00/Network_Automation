"""
____________________________________ AsyncIO & Telnet ______________________________________

* Setting Up and Establishing a Telnet Connection
* Sending Commands and Handling Responses

"""

import asyncio
import telnetlib3

async def shell(reader, writer):

    commands = [('Username: ', 'csn'),
                ('Password: ', 'cisco'),
                ('#', 'terminal length 0'),
                ('#', 'sh run'),
                ('#', 'exit'),]

    command_iter = iter(commands)
    expect, send = next(command_iter)

    while True:
        output = await reader.read(2048)
        if not output:
            break
        if expect in output:
            writer.write(f"{send}\n")
            try:
                expect, send = next(command_iter)
            except StopIteration:
                break

    print(output, flush=True)

loop = asyncio.get_event_loop()

coro = telnetlib3.open_connection('10.1.1.10',23,shell=shell)

reader, writer = loop.run_until_complete(coro)

loop.run_until_complete(writer.protocol.waiter_closed)
