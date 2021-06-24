n = int(input())
a = list(map(int, input().split()))
a.sort() # 공포도 낮은 순으로 정렬
count = 0 # 현 그룹의 포함 인원
result = 0 # 토탈 그룹 수

for i in a:
    count+=1 # 낮은 공포도 부터 검사
    if count >= i: # 현 그룹 포함 인원이 공포도보다 크거나 같으면
        result+=1 #그룹 결성
        count = 0 #현 그룹 초기화

print(result)
