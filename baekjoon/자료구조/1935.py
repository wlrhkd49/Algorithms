import sys
input = sys.stdin.readline
stack = []
n = int(input())
s = list(input().rstrip())
num = [0] * n

for i in range(n):
    num[i] = int(input())

for i in s:
    if i.isalpha():
        stack.append(num[ord(i)-ord('A')])
    else:
        x = stack.pop()
        y = stack.pop()
        if i == "+":
            stack.append(y+x)
        elif i == "*":
            stack.append(y*x)
        elif i == "-":
            stack.append(y-x)
        elif i == "/":
            stack.append(y/x)

print(format(stack[0],".2f"))
        