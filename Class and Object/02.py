class Details:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def call(self):
        return f"I am {self.name} and I am {self.age} years old"

info = Details("Rakib", 20)
information = info.call()
print(information)
