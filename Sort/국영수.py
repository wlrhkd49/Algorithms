n = int(input())
arr = []

for _ in range(n):
    arr.append((input().split()))

arr = sorted(arr, key = lambda x : (-int(x[1]), int(x[2]), -int(x[3]), x[0]))

for student in arr:
    print(student[0])