import sys
input = sys.stdin.readline
data = list(input().rstrip())
stack = []
result = 0

for i in range(len(data)):
    if data[i] == '(':
        stack.append('(')
    else:
        if data[i-1] == '(':
            stack.pop()
            result += len(stack)
        else:
            stack.pop()
            result += 1
print(result)