import asyncio
from concurrent.futures import ThreadPoolExecutor


async def custom_coro():
    print("this is a async coroutine")


loop = asyncio.new_event_loop()
loop.run_until_complete(custom_coro())
print(loop.is_running())


async def another_function():
    await asyncio.sleep(2)
    print("completed .....")


async def another_function_1():
    await asyncio.sleep(1)
    print("completed 1 .....")


# loop.close()
print(loop)
# define a task
coro = asyncio.sleep(2)
task = loop.create_task(custom_coro())
loop.run_until_complete(another_function())
loop.run_until_complete(another_function_1())

# This is because if the program exits while the event loop is running, a RuntimeWarning will be raised.
# loop.create_task(another_function())
print("after completed")
print('done')

# create an executor
with ThreadPoolExecutor() as exe:
    # execute a function in event loop using executor
    loop.run_in_executor(exe, task)

