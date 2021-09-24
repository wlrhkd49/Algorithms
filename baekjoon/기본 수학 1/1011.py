for _ in range(int(input())):
    x, y = map(int,input().split())
    i = 1
    result = y-x
    count = 0
    while result>0:
        if result-i <= 0 or result-(i-1) <= 0:
            count += 1
            break
        else:
            result -= 2*i
            count += 2
        i+=1
    print(count)