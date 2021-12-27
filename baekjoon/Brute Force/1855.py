n = int(input())
s = input()
answer = []
tmp = ''

for i in range(len(s)//n):
    if i % 2 == 1:
        tmp = s[i*n:i*n+n]
        # 오른쪽 -> 왼쪽
        answer.append(tmp[::-1])
    else:
        # 왼쪽 -> 오른쪽
        answer.append(s[i*n:i*n+n])

for i in range(n):
    for j in range(len(s)//n):
        print(answer[j][i], end='')