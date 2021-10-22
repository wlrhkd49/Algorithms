n = int(input())
data = list(map(int ,input().split()))
count = n
for d in data:
    if d == 1:
        count-=1
        continue
    for i in range(2,int(d**0.5)+1):
        if d % i == 0:
            count -= 1
            break

print(count)
