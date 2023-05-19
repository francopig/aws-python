def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True

# Find prime numbers between 1 and 250
prime_numbers = [number for number in range(1, 251) if is_prime(number)]

# Store results in a file
with open("results.txt", "w") as file:
    file.write("Prime numbers between 1 and 250:\n")
    for prime in prime_numbers:
        file.write(str(prime) + "\n")