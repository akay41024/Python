def fib_series(num_terms):
    fib = []
    a, b = 0, 1
    for _ in range(num_terms):
        fib.append(a)
        a, b = b, a + b
    return fib

n = int(input("Enter the number of terms in the Fibonacci series: "))

fib = fib_series(n)

print("Fibonacci series of", n, "terms is:", end=" ")

for i in fib:
    print(i, end=" ")
