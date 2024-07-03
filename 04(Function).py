# print(object(s), sep=separator, end=end, file=file, flush=flush)
a=7
b=8
print("The sum of",a, "and",b, "is",a+b,sep=" " , end=".\n")

def isGreater(a, b):
    if a>b:
        return a
    
    else :
        return b

greatest_Number = isGreater(5,7)
print(greatest_Number , "is the bigger Number")

def avarage(*numbers):
    print(type(numbers))
    sum = 0
    for i in numbers:
        sum = sum + i
    return sum/len(numbers)

print(avarage(58,36,98,4,552,4,5,74,5,514,4,65,54,54))

def Name(**names):
    print(type(names))
    return names['first_Name'] , names['middle_Name'] , names['last_Name']

my_Name =  Name(first_Name='MR.' , middle_Name='RAkib' , last_Name='Khan')
print("Hello ", my_Name)