numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
a= 1
b = 15
primes = []
not_primes = []
is_prime = True
for num in range(a, b+1):
    if(num > 1):
        for i in range(2, num):
            if(num % i) == 0:
                is_prime = False
                not_primes.append(num)
                break
        else:
            primes.append(num)
print(numbers)
print(not_primes)
print(primes)
