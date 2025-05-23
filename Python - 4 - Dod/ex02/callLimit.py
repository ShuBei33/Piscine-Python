from typing import Any


def callLimit(limit: int):
    # This will be the decorator factory
    def callLimiter(function):
        count = 0

        def limit_function(*args: Any, **kwds: Any):
            nonlocal count
            if count < limit:
                count += 1
                return function(*args, **kwds)
            else:
                print(f"Error: {function} call too many times")

        return limit_function

    return callLimiter
