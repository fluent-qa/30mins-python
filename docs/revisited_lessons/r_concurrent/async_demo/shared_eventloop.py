import asyncio


loop = asyncio.new_event_loop()
capture_context = {"index": 0}


async def task():
    print("start task")
    while True:
        capture_context["index"] = +1  # block


def run_task():
    t = loop.create_task(task())
    capture_context['task'] = t
    return t


def tag_task():
    print("stop task")
    t = capture_context['task']
    print(t)
    if t.done():
        print("task is done")
        # run_task()
    else:
        t.cancel()
        print("task is cancelled")


t = run_task()

tag_task()
print(capture_context["index"])

tag_task()
print(capture_context["task"])
