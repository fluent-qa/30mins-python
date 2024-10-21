from __future__ import annotations

import inspect
import json
import logging
from collections.abc import Callable

import requests
from requests import HTTPError


class ExceptionHandlerDecorator:
    def __init__(
        self,
        except_handler: Callable,
        except_handler_kwargs: dict = None,
        exception_type: Exception | tuple[Exception] = Exception,
        logger: logging.Logger = logging.getLogger(),
    ):
        """

        :param exp_handler:
        :param except_handler_kwargs:
        :param exception_type:
        :param logger:
        """
        self.except_handler = except_handler
        self.except_handler_kwargs = except_handler_kwargs
        self.exception_type = exception_type
        self.logger = logger

    @staticmethod
    def get_f_locals(func):
        frameinfo = None
        for _frameinfo in inspect.trace():
            if _frameinfo[3] == func.__name__:
                frameinfo = _frameinfo

        frame = frameinfo[0]
        return frame.f_locals

    @staticmethod
    def tryexcept(
        handled_function: Callable,
        handled_function_args: tuple,
        handled_function_kwargs: dict,
        except_handler: Callable,
        except_handler_kwargs: dict,
        exception_type: Exception | tuple[Exception],
        logger: logging.Logger,
    ):
        try:
            try_value = handled_function(
                *handled_function_args, **handled_function_kwargs
            )

            return try_value

        except exception_type as exception:
            f_exc = exception
            f_locals = ExceptionHandlerDecorator.get_f_locals(func=handled_function)
            f_name = handled_function.__name__

            except_handler_parameters = inspect.signature(except_handler).parameters

            if except_handler_parameters.get("f_exc"):
                except_handler_kwargs["f_exc"] = f_exc

            if except_handler_parameters.get("f_locals"):
                except_handler_kwargs["f_locals"] = f_locals

            if except_handler_parameters.get("f_name"):
                except_handler_kwargs["f_name"] = f_name

            logger.exception(
                "TryExcept decorator handled an exception. Traceback below."
            )

            except_value = except_handler(**except_handler_kwargs)

            return except_value

    def decorator(
        handled_function: Callable,
        except_handler: Callable,
        except_handler_kwargs: dict,
        exception_type: Exception,
        logger: logging.Logger,
        **kwargs,
    ):
        def wrapper(*handled_function_args, **handled_function_kwargs):
            return ExceptionHandlerDecorator.tryexcept(
                handled_function=handled_function,
                handled_function_args=handled_function_args,
                handled_function_kwargs=handled_function_kwargs,
                except_handler=except_handler,
                except_handler_kwargs=except_handler_kwargs,
                exception_type=exception_type,
                logger=logger,
            )

        return wrapper

    def __call__(
        self,
        func: Callable = None,
        exception_type=None,
    ):
        _kwargs = {
            "handled_function": func,
            "except_handler": self.except_handler,
            "except_handler_kwargs": self.except_handler_kwargs,
            "exception_type": exception_type or self.exception_type,
            "logger": self.logger,
        }

        wrapper = ExceptionHandlerDecorator.decorator(**_kwargs)

        return wrapper


def my_custom_exception_handling_function(
    f_exc: Exception, f_locals: dict, f_name: str, message: str
):
    print(f"Custom exception handler error message: {message}")
    print(f"Custom exception handler was called by the '{f_name}' function.")
    print(
        f"Available local variables in the callee namespace at the moment of exception: \n {json.dumps(obj=f_locals, indent=1, default=str)}"
    )
    print(f"The exception raised was of type {type(f_exc)}")
    return {"exc": f_exc, **f_locals, "message": message}


mytryexc = ExceptionHandlerDecorator(
    exception_type=HTTPError,
    except_handler=my_custom_exception_handling_function,
    except_handler_kwargs={"message": "There was an error!"},
)


@mytryexc
def get_data(url):
    response = requests.get(url)
    response.raise_for_status()
    return response.json()


def main():
    result = get_data(url="http://example.com/nonexistentpage.html")
    print(result)


if __name__ == "__main__":
    main()
    print("complete who running")
