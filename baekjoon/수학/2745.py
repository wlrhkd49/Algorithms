arr = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
N, B = input().split()
result = 0
N = N[::-1]
for i in range(len(N)):
    index = arr.index(N[i])
    result += index*pow(int(B), i)
print(result)