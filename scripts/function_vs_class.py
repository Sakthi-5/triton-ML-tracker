# Simple task: convert a name to uppercase


# Function approach
def normalize_name(name):
    return name.strip().upper()


name = " Alice "

result = normalize_name(name)

print("Function result:", result)