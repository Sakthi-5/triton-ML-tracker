from src.utils.decorators import retry


def test_retry_succeeds_after_failure():
    attempts = {"count": 0}

    @retry(max_attempts=3)
    def unstable_function():
        attempts["count"] += 1

        if attempts["count"] < 3:
            raise ValueError("Temporary failure")

        return "success"

    result = unstable_function()

    assert result == "success"
    assert attempts["count"] == 3


def test_retry_raises_after_max_attempts():
    attempts = {"count": 0}

    @retry(max_attempts=3)
    def failing_function():
        attempts["count"] += 1
        raise ValueError("Permanent failure")

    try:
        failing_function()
        assert False
    except ValueError:
        pass

    assert attempts["count"] == 3