x, y, w, h = map(int, input().split())

if x >= w//2+1 and y >= h//2+1:
    if (w-x) < (h-y):
        print(w-x)
    else:
        print(h-y)
elif x >= w//2+1 and y <= h//2+1:
    if (w-x) < y:
        print(w-x)
    else:
        print(y)
elif x <= w//2+1 and y <= h//2+1:
    if x < y:
        print(x)
    else:
        print(y)
elif x <= w//2+1 and y >= h//2+1:
    if x < (h-y):
        print(x)
    else:
        print(h-y)