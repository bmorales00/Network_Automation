"""
____________________________________ AsyncIO & Asynchronous Programming ______________________________________

* Setting Up and Writing an Async Function
* Running an Async Function
* Managing Multiple Tasks Concurrently

"""
import asyncio

async def say_hello():
    print("Hello")
    await asyncio.sleep(1)
    print("Hello again")

async def say_bye():
    print("Goodbye")
    await asyncio.sleep(2)
    print("Goodbye again")

async def main():
    await asyncio.gather(say_hello(),say_bye())


asyncio.run(main())


