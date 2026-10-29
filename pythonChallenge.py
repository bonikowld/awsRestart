def is_prime(n):
    if n < 2:
        return False

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False

    return True


# Find prime numbers between 1 and 250
primes = [num for num in range(1, 251) if is_prime(num)]

# Display primes on the screen
print("Prime numbers between 1 and 250:")
for prime in primes:
    print(prime)

# Save primes to results.txt
with open("results.txt", "w") as file:
    file.write("Prime numbers between 1 and 250:\n")
    for prime in primes:
        file.write(f"{prime}\n")

print("\nResults have been saved to results.txt")
