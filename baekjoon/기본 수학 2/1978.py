n = int(input())
data = list(map(int,input().split()))
count = 0

for x in data:
    isPrime = True
    for i in range(2, x//2+1):
        if x%i==0:
            isPrime = False
    if isPrime:
        count += 1
    if x == 1:
        count -= 1
print(count)