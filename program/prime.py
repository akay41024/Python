# def isPrime(n):
#     if n==1:
#         return False
#     elif n==2:
#         return True
#     else:
#         for i in range(2,n):
#             if n%i==0:
#                 return False
#         return True



# for i in range(1,5001):
#     if isPrime(i):
#         print(i, end=" ")

def isPrime(n):
    if n==1:
        return False
    elif n==2:
        return True
    else:
        for i in range(2,n):
            if n%i==0:
                return False
        return True

n = int(input("Enter the number: "))

if isPrime(n):
    print(n, "is a prime number")
else:
    print(n, "is not a prime number")






    