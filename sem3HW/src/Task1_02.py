class Person:
   

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print(self.name, self.age)

p1 = Person("Jon", 23)    
p2 = Person("Katty", 24)    

print(p1)
print(p2)

p1.introduce()
p2.introduce()