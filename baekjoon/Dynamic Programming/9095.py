d = [0] * 12
d[0] = 0
d[1] = 1 # 1
d[2] = 2 # 1+1, 2
d[3] = 4 # 1+1+1, 2+1, 1+2, 3
for i in range(4, 12):
    # 1,2,3 더하여 만드는 경우의 수를 모두 더함
    d[i] = d[i-1] + d[i-2] + d[i-3]
for i in range(int(input())):
    n = int(input())
    print(d[n])
