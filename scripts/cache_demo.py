from functools import lru_cache


@lru_cache(maxsize=3)
def expensive_operation(number):
    print(f"Calculating for {number}")
    return number * number


print(expensive_operation(5))
print(expensive_operation(5))
print(expensive_operation(10))
print(expensive_operation(10))