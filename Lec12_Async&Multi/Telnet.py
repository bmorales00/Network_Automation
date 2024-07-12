import asyncio
import telnetlib3


# Define a coroutine to handle the Telnet client behavior
async def shell(reader, writer):
    # Define the interaction rules with the Telnet server
    commands = [
        ('Username: ', 'csn'),  # Expect 'Username:', send username 'csn'
        ('Password: ', 'cisco'),  # Expect 'Password:', send password 'cisco'
        ('>', 'enable'),  # Expect '>', send 'enable'
        ('Password: ', 'cisco'),  # Expect 'Password:', send password 'cisco'
        ('#', 'terminal length 0'),  # Expect '#', send 'terminal length 0'
        ('#', 'show run'),  # Expect '#', send 'show run'
        ('#', 'exit'),  # Expect '#', send 'exit'
    ]
    command_iter = iter(commands)  # Create an iterator over the list of rules
    expect, send = next(command_iter)  # Get the first rule
    while True:
        output = await reader.read(2048)  # Read output from the Telnet server
        if not output:  # If there's no output (connection closed)
            break
        if expect in output:  # If expected string is found in output
            writer.write(f"{send}\n")  # Write the corresponding send string
            try:
                expect, send = next(command_iter)  # Get the next rule
            except StopIteration:
                break  # If no more rules, exit loop

    # Print the server output
    print(output, flush=True)


# Get the asyncio event loop
loop = asyncio.get_event_loop()

# Create a coroutine to open a Telnet connection
coro = telnetlib3.open_connection('10.1.1.10', 23, shell=shell)

# Run the coroutine until completion and get the reader and writer
reader, writer = loop.run_until_complete(coro)

# Run the event loop until the Telnet connection is closed
loop.run_until_complete(writer.protocol.waiter_closed)