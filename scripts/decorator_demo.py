from src.utils.decorators import retry


attempt_count = 0


@retry(max_attempts=3)
def unstable_operation():
    global attempt_count

    attempt_count += 1

    if attempt_count < 3:
        raise ValueError("Temporary failure")

    return "Operation successful"


result = unstable_operation()

print("Result:", result)