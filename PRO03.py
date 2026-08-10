#Program No 3: Use Logic Programming in Python to Check Prime Numbers
def is_prime(n):
    if n < 2:
        return False

    divisor = 2
    while divisor * divisor <= n:
        if n % divisor == 0:
            return False
        divisor += 1

    return True

number = 3

if is_prime(number):
    print(number, "is a prime number.")
else:
    print(number, "is not a prime number.")
