n = int(input())

data = list(map(int, input().split()))

data.sort()

print(data[int(len(data)/2)-1])