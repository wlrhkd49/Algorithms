n = int(input())
result = 0

for i in range(n):
    s = str(input())
    result = 0
    cnt = 0
    for j in range(len(s)):
        if s[j] == 'O':
            cnt += 1
        else:
            cnt = 0
        result += cnt
    print(result)
