x = int(input())

# 계산된 결과 저장 DP테이블
d = [0] * 30001

# DP 진행 (bottom-up)
for i in range(2, x+1):
    # 현재 수에서 1 빼는 경우
    d[i] = d[i-1] + 1
    # 현재의 수가 2로 나눠지는 경우
    if i % 2 == 0:
        d[i] = min(d[i], d[i//2]+1)
    # 현재의 수가 3로 나눠지는 경우
    if i % 3 == 0:
        d[i] = min(d[i], d[i//3]+1)
    # 현재의 수가 3로 나눠지는 경우
    if i % 5 == 0:
        d[i] = min(d[i], d[i//5]+1)

print(d[x])