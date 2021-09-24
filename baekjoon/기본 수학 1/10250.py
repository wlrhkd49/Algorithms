for _ in range(int(input())):
    a, b, c = map(int, input().split())
    h = c % a
    w = int(c/a) + 1
    if c % a == 0:
        w = int(c/a)
        h = a
    if len(str(w)) == 1:
        print(str(h)+'0'+str(w))
    else:
        print(str(h)+str(w))