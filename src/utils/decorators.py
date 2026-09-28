import time
from functools import wraps


def timeit(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()

        result = func(*args, **kwargs)

        end_time = time.perf_counter()

        elapsed_time = end_time - start_time

        print(f"{func.__name__} took {elapsed_time:.6f} seconds")

        return result

    return wrapper
def retry(max_attempts):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(1, max_attempts + 1):
                try:
                    return func(*args, **kwargs)
                except Exception as error:
                    print(
                        f"Attempt {attempt} failed: {error}"
                    )

                    if attempt == max_attempts:
                        raise

        return wrapper

    return decorator