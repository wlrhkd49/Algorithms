import sys
from collections import Counter
input = sys.stdin.readline

n = int(input())
data = []
for i in range(n):
    x = int(input())
    data.append(x)

data.sort()

# 산술 평균
print('%0.0f' % (sum(data)/n))
# 중간값
print(data[n//2])

# 가장 빈도수가 높은 숫자로 빈도수를 구한다.
# 빈도수가 높은 숫자 2개를 가져온다.
cnt = Counter(data).most_common(2) 

if len(data) > 1: # 데이터가 2개 이상 입력받을 경우
    if cnt[0][1] == cnt[1][1]:
        print(cnt[1][0])
    else:
        print(cnt[0][0])
else: # 데이터가 1개인 경우
    print(cnt[0][0])

# 최대값 - 최소값
print(data[n-1]-data[0])