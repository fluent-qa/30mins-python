import threading
from concurrent.futures import ThreadPoolExecutor
from random import random
from time import sleep

local_data = threading.local()


def thread_task():
    local_data.value = 'value in thread'
    print(local_data.value)


def main():
    local_data.value = 'value in main'
    print(local_data.value)
    thread = threading.Thread(target=thread_task)
    thread.start()
    thread.join()
    print(local_data.value)



if __name__ == '__main__':
    main()

