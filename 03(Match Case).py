"""match variable_name:
            case ‘pattern1’ : //statement1
            case ‘pattern2’ : //statement2
            …
            case ‘pattern n’ : //statement n
            case _ : //Else statement"""


x = int(input("Enter a digit : "))
# x is the variable to match
match x:
    # if x is 0
    case 0:
        print("x is zero")
    # case with if-condition
    case 4 if x % 2 == 0:
        print("x % 2 == 0 and case is 4")
    # Empty case with if-condition
    case _ if x < 10:
        print("x is < 10")
    # default case(will only be matched if the above cases were not matched)
    # so it is basically just an else:
    case _:
        print(x)