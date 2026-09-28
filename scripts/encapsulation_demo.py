class User:

    def __init__(self, name, age):
        self.name = name
        self._age = age
        self.__password = "secret123"

    def show_details(self):
        print("Name:", self.name)
        print("Age:", self._age)
        print("Password:", self.__password)


user = User("Alice", 22)

print("Public:", user.name)
print("Protected convention:", user._age)

user.show_details()

print("Private:", user.__password)