for _ in range(int(input())):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    r = ((x1-x2)**2 + (y1-y2)**2) ** 0.5
    maxR = max(r1, r2)
    minR = min(r1, r2)
    # 두 원이 일치하는 경우 -1
    if r == 0 and r1==r2:
        print(-1)
    # 두 원이 한점에서 만나는 경우 (외접, 내접)
    elif r1 + r2 == r or maxR == minR + r:
        print(1)
    # 두 원이 만나지 않는 경우
    elif r > r1+r2 or maxR > minR + r:
        print(0)
    # 이 외에 두점에서 만나는 경우
    else:
        print(2)
