class Person:
    # static properties
    total_persons = 0
    name = ""
    age = 0

    # constructor
    def __init__(self, name="", age=0):
        self.name = name
        self.age = age

    # static method
    @staticmethod
    def get_total_persons():
        return Person.total_persons


# call static method
Person.total_persons = 12
print(Person.get_total_persons())
