import logging
import time
from functools import wraps


logger = logging.getLogger(__name__)


def timeit(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()

        try:
            return func(*args, **kwargs)
        finally:
            elapsed_time = time.perf_counter() - start_time

            logger.info(
                "function completed",
                extra={
                    "function": func.__name__,
                    "duration_seconds": elapsed_time,
                },
            )

    return wrapper


def retry(max_attempts):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(1, max_attempts + 1):
                try:
                    return func(*args, **kwargs)

                except Exception:
                    logger.exception(
                        "function attempt failed",
                        extra={
                            "function": func.__name__,
                            "attempt": attempt,
                            "max_attempts": max_attempts,
                        },
                    )

                    if attempt == max_attempts:
                        raise

        return wrapper

    return decorator