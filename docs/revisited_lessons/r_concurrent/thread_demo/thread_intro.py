import multiprocessing
import threading
from multiprocessing import current_process

capture_context = {"index": 0}

signal = True
print(current_process().name+":"+str(current_process().pid.real))

## Process
## Thread
## Async
def task():
    print("start task")
    while signal:
        capture_context["index"] += 1  # block
        print(capture_context["index"])


thread = threading.Thread(target=task)
import multiprocessing as mp
mp.set_start_method('spawn')
child = mp.Process(target=task)
child.start()
print(child.name+str(child.pid.real))
child.terminate()
# mp.set_start_method('spawn')
# child = mp.Process(target=task)
# child.daemon =True
# child.start()

# child.close()


def start_thread():
    signal = True
    child.run()


def stop_thread():
    signal = False
    child.close()


# task executed by new processes
def process_task():
    # configure new threads
    threads = [threading.Thread(target=task) for _ in range(3)]
    # start new threads
    for thread in threads:
        thread.start()
    # wait for threads to finish
    for thread in threads:
        thread.join()
    # report message
    process_name = current_process().name
    print(f'Process {process_name} done.', flush=True)

# start_thread()
# stop_thread()
