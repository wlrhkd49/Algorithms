n, m, k = map(int, input().split())
data = list(map(int, input().split()))

data.sort()
first = data[n-1] #가장 큰 수
second = data[n-2] #두 번째로 큰 수

sum = 0

while True:
    for i in range(k): # 가장 큰 수 k번 더하기
        if m == 0:
            break
        sum += first
        m -= 1
    if m == 0:
        break
    sum += second # 가장 큰 수 k번 더하고 두 번째로 큰 수 한 번 더하기
    m -= 1

print(sum)