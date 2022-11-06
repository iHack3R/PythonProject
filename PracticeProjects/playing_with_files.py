# File read/write in Python

file = open("test_file.txt", "w")
file.write("Example")
file.close()

file = open("test_file.txt", "r")
for each in file:
    print(each)
