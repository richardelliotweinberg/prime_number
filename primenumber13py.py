def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

num = int(input("Enter a Number: "))

if is_prime(num):
    print(num, "is Prime.")
else:
    print(num, "is composite.")

#print("Prime numbers up to 10000:")
#for i in range(2, 10001):
#    if is_prime(i):
#        print(i)
