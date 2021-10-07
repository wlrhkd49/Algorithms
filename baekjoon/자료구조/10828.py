import sys
input = sys.stdin.readline
stack = []

for _ in range(int(input())):
    command = input().split()
    if command[0] == 'push': # push 일 경우
        stack.append(int(command[1])) # stack에 저장
    elif command[0] == 'pop': # pop 일 경우
        if len(stack) == 0: 
            print(-1)
        else:
            print(stack.pop())
    elif command[0] == 'size': # size 일 경우
        print(len(stack))
    elif command[0] == 'empty': # empty 일 경우
        if len(stack) == 0:
            print(1)
        else:
            print(0)
    else: # top 일 경우
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1])