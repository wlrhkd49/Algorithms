import sys
input = sys.stdin.readline

def gcd(x, y):
    if y == 0:
        return x
    else:
        return gcd(y, x%y)

n, s = map(int, input().split())
bros = list(map(int, input().split()))
diff = []
for b in bros:
    diff.append(abs(s-b))
    
x = diff[0]

for d in diff:
    x = gcd(x, d)
    
print(x)
