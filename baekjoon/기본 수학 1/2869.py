a, b, v = map(int, input().split())

# 올라가는데 걸리는 일수 구하기
num = (v-b) / (a-b)

if num == int(num):
    print(int(num))
else:
    print(int(num)+1)