n = int(input())
count = n
for _ in range(n):
    x = input()
    for i in range(len(x)-1):
        if x[i] != x[i+1]:
            new_x = x[i+1:]
            if new_x.count(x[i])>0:
                count -= 1
                break
print(count)

