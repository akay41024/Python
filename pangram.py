pangram = input("Enter a string: ")

if(len(set(pangram.lower())) == 26):
    print("Pangram")
else:
    print("Not a Pangram")

    