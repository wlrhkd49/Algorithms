a, b = map(int, input().split())
data = list(map(int, input().split()))

arr = [0] * 10 # 무게 0~10까지 배열 만들기

for i in data:
    # 각 무게에 해당되는 볼링공 개수 카운트
    arr[i] += 1

result = 0

for i in range(1, b+1):
    a -= arr[i] # 무게 i인 볼링공 개수 제외
    result += arr[i] * a # 무게 i인 볼링공 개수 x B가 선택하는 개수

print(result)