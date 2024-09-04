n = int(input())

result = ''
for i in range(1, n + 1):
    for cc in range(1, n + 1):
        if n % (cc + i) == 0 and cc > i:
            result += f'{i}{cc}'
print(result)
