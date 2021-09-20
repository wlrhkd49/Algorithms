n = int(input())
result = 0

for i in range(n):
    s = str(input())
    result = 0
    count = 0
    for j in range(len(s)):
        if s[j] == 'O':
            count += 1
        else:
            count = 0
        result += count
    print(result)