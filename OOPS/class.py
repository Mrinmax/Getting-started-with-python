class myClass():
    x = 5
    print("This is my class")



#main oops concent and declaration
#The __init__() function is called automatically every time the class is being used to create a new object

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p1 = Person("Mrinal", 24)

print(p1.name)
print(p1.age)

