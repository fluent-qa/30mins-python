from loguru import logger
import sys


@logger.catch
def my_function(x, y, z):
    # An error? It's caught anyway!
    return 1 / (x + y + z)


def set_up_sys_logger():
    logger.add(sys.stderr, format="{time} {level} {message}", filter="loguru_demo", level="INFO")
    logger.add("file_1.log", rotation="500 MB")  # Automatically rotate too big file
    logger.add("file_2.log", rotation="12:00")  # New file is created each day at noon
    logger.add("file_3.log", rotation="1 week")  # Once the file is too old, it's rotated
    logger.add("file_{time}.log", retention="10 days")  # Cleanup after some time
    logger.add("file_Y.log", compression="zip")  # Save some loved space


def log_different_level():
    logger.info("this is test")
    logger.warning("this is test")
    logger.debug("this is test")
    logger.trace("this is test")
    logger.error("this is error test")
    logger.info("If you're using Python {}, prefer {feature} of course!", 3.6, feature="f-strings")
    logger.add(sys.stdout, colorize=True, format="<green>{time}</green> <level>{message}</level>")


if __name__ == '__main__':
    set_up_sys_logger()
    log_different_level()
    my_function(1, 2, -3)
