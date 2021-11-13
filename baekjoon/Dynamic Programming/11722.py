# n = int(input())
# data = list(map(int, input().split()))
# dp = [1] * (n+1)

# for i in range(len(data)):
#     for j in range(i):
#         if data[j] < data[i]:
#             dp[i] = max(dp[i], dp[j]+1)

# print(max(dp))

n = int(input())

data = list(map(int, input().split()))
dp = [1] * (n+1)

data.reverse()

for i in range(len(data)):
    for j in range(i):
        if data[j] < data[i]:
            dp[i] = max(dp[i], dp[j]+1)

print(max(dp))