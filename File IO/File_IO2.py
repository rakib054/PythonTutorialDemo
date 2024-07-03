### readline() method
file = open("E:\Python Project\File IO\IRIS\iris_data.data" , 'r')

while True:
    line = file.readline().strip()    # I use ,strip() to remove any leading or trailing whitespace characters, including the newline character
    if not line:
        break
    sepal_length = float(line.split(',')[0])
    sepal_width = float(line.split(',')[1])
    petal_length = float(line.split(',')[2])
    petal_width = float(line.split(',')[3])
    name = line.split(',')[4]
    # print(f"The flower {name}'s Length is : {sepal_length} , Width is : {sepal_width}\nPetal Length is : {petal_length} , Petal Width is : {petal_width}\n\n")



### writelins() method
with open("my_file4.txt", 'w') as file:
    lines = []
    for i in range (1,101):
        if i<10:
            lines.append(f"Line 0{i}\n")
        else:
            lines.append(f"Line {i}\n")          
    
    file.writelines(lines)
