from contextlib import contextmanager


@contextmanager
def managed_resource():
    print("Resource acquired")

    try:
        yield
    finally:
        print("Resource released")