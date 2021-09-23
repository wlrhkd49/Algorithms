a, b, c = map(int, input().split())
i = 1
if b >= c:
    i = -1
else:
    i = a // (c - b) + 1
    
print(i)