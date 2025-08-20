# Program to check if a number is even, odd, and prime


def is_even(number):
    return number % 2 == 0


def is_odd(number):
    return number % 2 != 0


def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True


num = int(input("Enter a number: "))

if is_even(num):
    print(f"{num} is even.")
else:
    print(f"{num} is odd.")

if is_prime(num):
    print(f"{num} is prime.")
else:
    print(f"{num} is not prime.")
