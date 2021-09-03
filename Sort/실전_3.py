n = int(input())

data = []
for i in range(n):
    data.append(input().split())

def sort(array):
    return int(array[1])

result = sorted(data, key = sort)

for a in result:
    print(a[0], end = ' ')

