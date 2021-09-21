numbers = list(range(1, 10001))
remove_list = [] # 이후에 삭제할 리스트
for num in numbers:
    for n in str(num):
        num += int(n)
    if num<=10000:
        remove_list.append(num)

for remove_num in set(remove_list): # set으로 중복값 제거
    numbers.remove(remove_num) # 생성자가 없는 숫자 제거
for self_num in numbers:
    print(self_num)