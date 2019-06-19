class Person:
    firstname = None
    lastname = None

    def __str__(self):
        firstname = "Mesut"
        return firstname

p1 = Person()

print(p1.__str__())

