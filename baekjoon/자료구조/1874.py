import sys
input = sys.stdin.readline
count = 0
stack = []
result = []
tmp = True

for _ in range(int(input())):
    x = int(input())

    while count < x:
        count += 1
        stack.append(count)
        result.append('+')

    if stack[-1] == x:
        stack.pop()
        result.append('-')
    else:
        tmp = False

if tmp == False:
    print('NO')
else:
    for r in result:
        print(r)
    