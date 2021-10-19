import sys
input = sys.stdin.readline
while True:
    data = [0] * (4)
    # input중에서 \n 개행은 제외한다.
    s = input().rstrip("\n")
    if not s:
        break
    else:
        for i in s:
            if i.islower():
                data[0] += 1
            elif i.isupper():
                data[1] += 1
            elif i.isnumeric():
                data[2] += 1
            else:
                data[3] += 1
        for i in range(len(data)):
            print(data[i], end= ' ')
        print()
    
