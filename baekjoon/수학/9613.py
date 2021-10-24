from itertools import combinations
import sys
input = sys.stdin.readline

def gcd(x, y):
    if y == 0:
        return x
    else:
        return gcd(y, x%y)
for _ in range(int(input())):
    data = list(map(int, input().split()))
    result = 0
    for x in list(combinations(data[1:], 2)):
        result += gcd(x[0], x[1])

    print(result)
