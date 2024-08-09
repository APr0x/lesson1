print('Enter 3 figures, each separately')
a = int(input())
print(a)
b = int(input())
print(b)
c = int(input())
print(c)
if a == b and b == c and a == c:
    print('3')
elif a == b or b == c or c == a:
    print('2')
else:
    print('0')
