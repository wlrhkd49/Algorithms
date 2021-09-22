x, y = input().split()

# x, y문자열 뒤집기
x = x[::-1]
y = y[::-1]

if int(x) < int(y):
    print(y)
else:
    print(x)
