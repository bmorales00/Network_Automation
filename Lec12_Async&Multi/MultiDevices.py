import asyncio
import telnetlib3


async def handle_prompt(reader, writer):
    commands = [
        ('>', 'enable'),
        ('#', 'terminal length 0'),
        ('#', 'show run'),
        ('#', 'exit'),
    ]
    command_iter = iter(commands)
    expect, send = next(command_iter)
    while True:
        outp = await reader.read(2048)
        if not outp:
            break
        if "Username:" in outp:
            writer.write('csn\n')
        elif "Password:" in outp:
            writer.write('cisco\n')
        elif expect in outp:
            writer.write(f"{send}\n")
            try:
                expect,send = next(command_iter)
            except StopIteration:
                break
        await writer.drain()
    await asyncio.sleep(1)
    print(f"{outp.strip()}\n", flush=True)


async def connect_to_router(host, port):
    try:
        reader, writer = await telnetlib3.open_connection(host, port)
        await handle_prompt(reader, writer)
        writer.close()
    except Exception as e:
        print(f"An error occurred while connecting to {host}: {e}")


async def main():
    routers = [
        ('10.1.1.10', 23),
        ('10.1.1.20', 23),
        ('10.1.1.30', 23)
    ]

    tasks = [connect_to_router(host, port) for host, port in routers]
    await asyncio.gather(*tasks)


asyncio.run(main())