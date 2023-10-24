class Person:
    name = "joe"
    age = 31
    gender = "male"

    def eat(self):
        print("eating")


p = Person() # instantiating an object
print(p.gender)
print(p.name)

p.eat()