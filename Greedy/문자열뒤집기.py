a = input()
c1 = 0
c2 = 0

# 처음 문자확인하고 카운트 증가
if a[0] == '0':
    c1 += 1
else:
    c2 += 1

# 모든 문자열 하나씩 돌면서
for i in range(len(a)-1):
    if a[i]!=a[i+1]: # 문자가 바뀐 경우
        if a[i+1] == '0': # 문자가 0 으로 바뀌면 c1 카운트 증가
            c1+=1
        else: # 1로 바뀌면 c2 카운트 증가
            c2+=1

print(min(c1,c2)) # 둘 중 최소값 출력