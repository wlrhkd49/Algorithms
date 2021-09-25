def isPrime(num):
    if num==1:
        return False
    else:
        for i in range(2, int(num**0.5)+1):
            if num%i == 0:
                return False
        return True

m, n = map(int, input().split())

for i in range(m, n+1):
    if isPrime(i):
        print(i)

## 배열에 삽입하고 출력하는 경우 시간 초과를 받음
