import time

import requests
import retry


def retry_it(max_retries, wait_time):
    def decorator(func):
        def wrapper(*args, **kwargs):
            retries = 0
            if retries < max_retries:
                try:
                    print(f"Retry Function {func.__name__}{args} {kwargs} ")
                    result = func(*args, **kwargs)
                    return result
                except Exception:
                    retries += 1
                    time.sleep(wait_time)
            else:
                raise Exception(f"Max retries of function {func} exceeded")

        return wrapper

    return decorator


def catch_it(exception_set):
    def decorator(func):
        def wrapper(*args, **kwargs):
            try:
                func(*args, **kwargs)
            except exception_set:
                print("catch exception")
            return wrapper

        return decorator


@retry_it(max_retries=5, wait_time=1)
def example_function():
    # function that may raise an exception
    print("Example function")


@retry.retry((ValueError, TypeError), delay=5, tries=6)
def check_status(id):
    response = requests.get("https://www.baidu.com")
    if response.status_code == 200:
        print(f"Status Code: {response.status_code}")
        raise ValueError("Response Value is 200, but not expected")
    else:
        return False


@catch_it(Exception)
@retry.retry((ZeroDivisionError, TypeError), delay=5, tries=6)
def div_zero():
    print("Divide Zero")
    return 1 / 0


def get_data(id):
    status = None
    while status is None or status == False:
        time.sleep(5)
        status = check_status(id)
    response = requests.get("https://www.baidu.com")
    return response


if __name__ == "__main__":
    example_function()
    try:
        check_status(1)
    except Exception as e:
        print(e)
    div_zero()
