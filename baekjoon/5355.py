for i in range(int(input())):
    a = list(input().split())
    result = 0
    
    for i in range(0, len(a)):
        if a[i] == '@':
            result *= 3
        elif a[i] == '%':
            result += 5
        elif a[i] == '#':
            result -= 7
        else:
            result = float(a[0])
    print("{:.2f}".format(result))
