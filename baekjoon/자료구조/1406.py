import sys
input = sys.stdin.readline
stack1 = list(input().strip())
stack2 = []

for _ in range(int(input())):
    command = input().split()
    if command[0] == "P":
        stack1.append(command[1])
    elif command[0] == "L" and len(stack1) != 0:
        stack2.append(stack1.pop())
    elif command[0] == "D" and len(stack2) != 0:
        stack1.append(stack2.pop())
    elif command[0] == "B" and len(stack1) != 0:
        stack1.pop()

print("".join(stack1 + list(reversed(stack2))))