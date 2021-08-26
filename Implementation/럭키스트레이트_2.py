n = input()
a = 0
b = 0
for i in range(int(len(n)/2)):
    a += int(n[i])

for j in range(int((len(n)/2)), len(n)):
    b += int(n[j])
print(a, b)
if a == b:
    print("LUCKY")
else:
    print("READY")
