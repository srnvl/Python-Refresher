with open("sample.txt" ,"r") as f:
    # data = f.read() # Reads the file and prints as it is
    # data = f.readlines() # Reads the file and prints it as a list of lines
    # data = f.readline() # Reads the file and prints the first line
    for line in f:
        print(line, end = '')
# print(data)

file = open("sample.txt" ,"r")
print(file.read(8)) # prints the first word 

with open("sample.txt", "r") as f:
    data = f.readlines()
    for line in data:
        word1 = line.split()
        word2 = line.splitlines()
    print(word1)
    print(word2)
