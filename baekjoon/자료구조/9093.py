import sys
input = sys.stdin.readline
for _ in range(int(input())):
    data = list(input().split())
    reversed_data = []
    for d in data:
        reversed_data.append(d[::-1])
    print(" ".join(reversed_data))
