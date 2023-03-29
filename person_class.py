class Person:
    """
    Create a class Person with attributes name and age,
    and a method greet() that prints a greeting message
    containing the person's name and age.
    Create an instance of the class and call the greet() method.
    """

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print(f"Greetings from Poland, {self.name}! You are {self.age} years old!")


if __name__ == "__main__":
    dawid = Person("Dawid", 30)
    dawid.greet()
