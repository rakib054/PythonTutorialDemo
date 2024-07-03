###Format Strings
name = "Guzman"
age = 18
statement = "My name is {} and my age is {}."
print(statement.format(name, age)) 

quantity = 2
fruit = "Apples"
cost = 120.0
statement = "I want to buy {2} dozen {0} for {1}$"
print(statement.format(fruit,cost,quantity))

txt = "For only {price:.2f} dollars!(Using Format strings)"
print(txt.format(price = 49.5465146))


### Now , you can use F-strings
letter = "Hey my name is {1} and I am from {0}"
country = "India"
name = "Harry"
print(f"Hey my name is {name} and I am from {country}")

price = 49.5465146
txt = f"For only {price:.2f} dollars!(Using F-strings)"
print(txt)

print(f"We use f-strings like this: Hey my name is {{name}} and I am from {{country}}")

print(f"{2 * 30}")