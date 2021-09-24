n = int(input())
sum_number = 1
count = 1

while n > sum_number:
    # 몇번째 줄인지 확인
    count += 1
    sum_number += count

# 몇번째 떨어진 index 인지 확인
x = sum_number - n

# 짝수번째 줄일 경우 1/n 부터 시작
if count % 2 == 0:
        print(str(count-1*x)+'/'+str(1+1*x))
# 홀수번째 줄일 경우 n/1 부터 시작
else:
        print(str(1+1*x)+'/'+str(count-1*x))