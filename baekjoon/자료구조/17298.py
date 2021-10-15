num = int(input())
data = list(map(int, input().split()))
stack = []
result = [-1 for _ in range(num)]
stack.append(0)
for i in range(num):
    while data[stack[-1]] < data[i]:
        result[stack.pop()] = data[i]
    stack.append(i)

for r in result:
    print(r, end= ' ')