def count_case(file_path):
    lowercount = 0
    uppercount = 0
    try:
        f = open(file_path, "r")    
        for line in f:
            for letter in line:
                if letter.islower():
                    lowercount += 1
                elif letter.isupper():
                    uppercount += 1
        return lowercount, uppercount
    except FileNotFoundError:
        print("File not found")
        return 0, 0


file_path = "Story.txt"

lowercase, uppercase = count_case(file_path)

print("Lowercase: ", lowercase)
print("Uppercase: ", uppercase)