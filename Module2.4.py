numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
is_prime = True
lower = 2
upper = 15
for i in numbers:
    if i > 1 and (i % 2) == 0:
        is_prime = False
        not_primes.append(i)
for j in range(lower, upper):
    if (upper % lower) != 0 and (j % 2) != 0 and j > 1:
        primes.append(j)
print(numbers)
print(not_primes)
print(primes)
