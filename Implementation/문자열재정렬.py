n = input()
arr = []
result = 0

# 문자 하나씩 확인
for i in range(len(n)):
    # 문자열이면 arr에 추가
    if(n[i].isalpha()):
        arr.append(n[i])
    # 숫자이면 더하기
    else:
        result+=int(n[i])

arr.sort()
# 숫자가 하나라도 존재하면 arr에 더하기
if result!=0:
    arr.append(str(result))

for i in range(len(arr)):
    print(arr[i], end ='', sep='')

print(''.join(arr))

