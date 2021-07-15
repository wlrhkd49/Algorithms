# 한 번 계산된 결과를 Memoization하기 위한 리스트 초기화
d = [0] * 100

# 피보나치 함수를 재귀함수로 구현 (top-down DP)
def fibo(x):
    if x == 1 or x == 2:
        return 1
    # 이미 계산한 문제라면 리스트에서 반환
    if d[x] != 0:
        return d[x]
    # 처음 계산한 문제라면 점화식에 따라 피보나치 결과 반환
    else:
        d[x] = fibo(x-1) + fibo(x-2)
        return d[x]

print(fibo(99))