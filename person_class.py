class Person:
    """
    Create a class Person with attributes name and age,
    and a method greet() that prints a greeting message
    containing the person's name and age.
    Create an instance of the class and call the greet() method.
    """

    def __init__(self, name, age):
        self._name = name
        self._age = age

    def greet(self):
        print(f"Greetings from Poland, {self.name}! You are {self.age} years old!")

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if value == "":
            raise ValueError("Name cannot be an empty string!")
        self._name = value

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if value <= 0:
            raise ValueError("Age cannot be less than 0!")
        self._age = value


if __name__ == "__main__":
    john = Person("John", 55)
    john.greet()
    # john.name = ""
    # john.age = 0
