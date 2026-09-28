from src.utils.resource_manager import managed_resource


try:
    with managed_resource():
        print("Using resource")
        raise ValueError("Something went wrong")

except ValueError as error:
    print("Caught error:", error)