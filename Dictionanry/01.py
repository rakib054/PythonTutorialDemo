info = {'name':'Karan', 'age':19, 'eligible':True}
print(info['name'])    # If Key is not defined in info , output will show KeyError
print(info.get('eligible'))    # If Key is not defined in info , output will show 'None' , cause here get() method is used

print(info.keys())
print(info.values())
print(info.items())    # items() method create touple of keys and values
print(info.__getitem__('name'))

### Using keys and values in for loop 
for key in info.keys():
    print(f"The value of {key} is {info.get(key)}")

# Creating touple of keys and values using items() method
for key, value in info.items():
    print(f"The value of {key} is {value}")