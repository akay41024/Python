num = 0
word = 0
char = 0
line = 0

file_path = "Story.txt"

try:
    f = open(file_path, "r")
    for i in f: 
        line += 1
        word += len(i.split())
        char += len(i)
        for j in i:
            if j.isnumeric():
                num += 1
    print("Number of lines: ", line)
    print("Number of words: ", word)
    print("Number of characters: ", char)
    print("Number of digits: ", num)
except FileNotFoundError:
    print("File not found")
    exit(0)
    