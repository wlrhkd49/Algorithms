n = int(input())
data = list(map(int,input().split()))
add, sub, mul, div = map(int, input().split())

min_result = 1e9
max_result = -1e9

def dfs(i, now):
    global add, sub, mul, div, min_result, max_result
    if i == n:
        min_result = min(min_result, now)
        max_result = max(max_result, now)
    
    else:
        # 각 연산자에 대해 재귀적으로 수행하여 모든 경우의 수를 찾음
        if add>0:
            add-=1
            dfs(i+1, now + data[i])
            add+=1
        if sub>0:
            sub-=1
            dfs(i+1, now - data[i])
            sub+=1
        if mul>0:
            mul-=1
            dfs(i+1, now * data[i])
            mul+=1
        if div>0:
            mul-=1
            dfs(i+1, int(now / data[i]))
            mul+=1

dfs(1,data[0])

print(max_result)
print(min_result)
