n = input()
data = [-1] * 26
for i in range(len(n)):
    if data[ord(n[i])%97] != -1:
        continue
    else:
        data[ord(n[i])%97] = i

for i in data:
    print(i, end=' ')