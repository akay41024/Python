def sum_of_N(n):
    if n == 1:
        return 1
    else:
        return n + sum_of_N(n-1)


n = int(input())

s = sum_of_N(n)

print(s)