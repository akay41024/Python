from functools import reduce

def find_max(x, y):
    return x if x > y else y

numbers = [1,2,3,45,6,7,78,89,90]

largest = reduce(find_max, numbers)
print(largest)