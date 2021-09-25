n = int(input())
prime_factor = []
i = 2

while n!=1:
    if n % i == 0:
        prime_factor.append(i)
        n = n//i
    else:
        i += 1

for data in prime_factor:
    print(data)