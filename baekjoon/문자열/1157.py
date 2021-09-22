# 문자열을 대문자로 변경
data = input().upper()
# 중복 제거
data_set = set(list(data))
max_number = 0

for i in data_set:
    if max_number < data.count(i):
        max_number = data.count(i)
        max_alphaget = i
data_set.remove(max_alphaget)

for i in data_set:
    if max_number == data.count(i):
        max_alphaget = '?'

print(max_alphaget)