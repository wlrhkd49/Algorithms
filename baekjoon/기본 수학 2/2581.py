m = int(input())
n = int(input())
prime = []
for i in range(m, n+1):
    isPrime = True
    if i == 1:
        continue
    for j in range(2, i//2+1):
        if i%j == 0:
            isPrime = False
    if isPrime:
        prime.append(i)
        
if len(prime) == 0:
    print(-1)
else:
    print(sum(prime))
    print(min(prime))
