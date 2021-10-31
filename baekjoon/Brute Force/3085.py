def check(data):
    result = 1
    for i in range(len(data)):
        cnt = 1
        for j in range(1, n):
            if data[i][j] == data[i][j-1]:
                cnt += 1
            else:
                cnt = 1
            if cnt > result:
                result = cnt
        cnt = 1
        for j in range(1, n):
            if data[j][i] == data[j-1][i]:
                cnt += 1
            else:
                cnt = 1
            if cnt > result:
                result = cnt
    
    return result
        
n = int(input())
data = []
result = 0
for i in range(n):
    data.append(list(input()))

for i in range(n):
    for j in range(n):
        if j < n-1:
            data[i][j], data[i][j+1] = data[i][j+1], data[i][j] # 좌우
            cnt = check(data)
            if cnt >= result:
                result = cnt
            data[i][j], data[i][j+1] = data[i][j+1], data[i][j] # 원위치
        if i < n-1:
            data[i][j], data[i+1][j] = data[i+1][j], data[i][j] # 상하
            cnt = check(data)
            if cnt >= result:
                result = cnt
            data[i][j], data[i+1][j] = data[i+1][j], data[i][j] # 원위치
            
print(result)
