numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
is_prime = True

for i in numbers:
    if (i % 2) == 0 and i > 1:
            is_prime = False
            not_primes.append(i)
    else:
            primes.append(i)

print(numbers)
print(not_primes)
print(primes)
