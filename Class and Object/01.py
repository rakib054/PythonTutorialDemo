class Details:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def call(self):
        return f"I am {self.name} and I am {self.age} years old"

info1 = Details("Rakib", 20)
info2 = Details("John", 25)
info2.age= 20
info3 = Details("Emma", 30)
info4 = Details("David", 22)
info5 = Details("Sarah", 28)

print(info1.call())
print(info2.call())
print(info3.call())
print(info4.call())
print(info5.call())