from datetime import datetime
from functools import wraps
from typing import Callable, Union


def logger(arg: Union[Callable, str, None] = None):
    """
    Универсальный декоратор:
    1) @logger                 -> пишет в main.log
    2) @logger("custom.log")   -> пишет в custom.log
    """

    def decorator(old_function: Callable, path: str):
        @wraps(old_function)
        def new_function(*args, **kwargs):
            called_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            result = old_function(*args, **kwargs)

            log_line = (
                f"[{called_at}] "
                f"function={old_function.__name__} "
                f"args={args} kwargs={kwargs} "
                f"result={result}\n"
            )

            with open(path, "a", encoding="utf-8") as f:
                f.write(log_line)

            return result

        return new_function

    # Случай: @logger без скобок
    if callable(arg):
        return decorator(arg, "main.log")

    # Случай: @logger("file.log") или @logger() (arg=None)
    path = arg if isinstance(arg, str) else "main.log"

    def __logger(old_function: Callable):
        return decorator(old_function, path)

    return __logger
