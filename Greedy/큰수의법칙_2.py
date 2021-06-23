n, m, k = map(int, input().split())
data = list(map(int, input().split()))

data.sort()
first = data[n-1] #가장 큰 수
second = data[n-2] #두 번째로 큰 수

#count는 가장 큰 수가 더해지는 횟수
count = (m//(k+1)) * k
count += m%(k+1)

sum = 0
sum += count * first # 가장 큰 수 덧셈 합
sum += (m-count) * second # 두 번째로 큰 수 덧셈

print(sum)