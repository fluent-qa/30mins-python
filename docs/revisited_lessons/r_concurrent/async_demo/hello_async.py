import asyncio

# hello world program for asyncio that tries to sleep
import asyncio

asyncio.sleep(1)

# define a coroutine
async def custom_coroutine():
    # block
    await asyncio.sleep(1)
    # report a message
    print('Hello world')


## Thread/Process/Coroutine

## start an event-loop 
asyncio.run(custom_coroutine())

print(asyncio.get_event_loop())
