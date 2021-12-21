N = input()
F = int(input())

for i in range(100):
    if i // 10 == 0:
        num = '0' + str(i)
        x = N[:-2] + num
    else:
        num = str(i)
        x = N[:-2] + str(i)
    if int(x) % F == 0:
        print(num)
        break

