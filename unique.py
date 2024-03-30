lst = ["a", "c", "c", "a", "e", "h", "g", "h", "j", "j"]

unique = []

for i in lst:
    if i not in unique:
        unique.append(i)
print(unique)   