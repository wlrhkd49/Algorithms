E, S, M = map(int, input().split())
n = 0
e, s, m = 0, 0, 0
while True:
    n += 1
    e = (e+1) % 16 if (e+1) % 16 != 0 else 1
    s = (s+1) % 29 if (s+1) % 29 != 0 else 1
    m = (m+1) % 20 if (m+1) % 20 != 0 else 1
    if e == E and s == S and m == M:
        print(n)
        break
    
