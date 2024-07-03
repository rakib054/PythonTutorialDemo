class Compare:
    # Without StaticMathod
    def check(self, a, b):
        self.a= a    # Define self.a & self.b
        self.b= b
        if self.a >= self.b:   # Even when checking , declaring self.a and self.b
            return True
        else:
            return False

class Math():
    @staticmethod    # With StaticMethod
    def check(a, b):    # No self.a or self.b
        if a >= b:    # Easily using a , b without self.....
            return True
        else:
            return False

obj1 = Compare()
obj2= Math()

# while True:
a= int(input("a : "))
b= int(input("b : "))

if obj1.check(a, b) is True:
    print("a is greater than or equal to b")
else:
    print("b is greater than a")
if obj2.check(a, b) is True:
    print("a is greater than or equal to b\n")
else:
    print("b is greater than a\n")
    