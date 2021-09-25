def isPrime(num):
    if num == 1:
        return False
    else:
        for i in range(2, int(num**0.5)+1):
            if num % i == 0:
                return False
        return True

for _ in range(int(input())):
    num = int(input())
    for i in range(num//2+1, -1, -1):
        if isPrime(num-i) and isPrime(i):
            if num-i > i:
                print(i, num-i)
            else:
                print(num-i, i)
            break
