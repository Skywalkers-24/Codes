class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

people = [Person("John Doe", 21), Person("Jane Doe", 22)]
people.sort(key=lambda person: person.name)
print(people)
