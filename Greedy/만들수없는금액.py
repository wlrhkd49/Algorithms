n = int(input())
a = list(map(int, input().split()))
a.sort()
target = 1 # 만들 수 있는 값

for i in a:
    # 화폐 단위보다 target이 작으면 멈춤! -> 더 이상 못만듬
    if target < i:
        break
    # 화폐 단위보다 target이 크면 화폐 단위 만큼 더함 -> 
    # 그 아래의 값들은 만들기 가능
    target+=i

print(target)