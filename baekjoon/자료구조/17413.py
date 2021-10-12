import sys
input = sys.stdin.readline

data = list(input().rstrip())
i = 0
start = 0

while i < len(data):
    # 괄호 부분은 그냥 인덱스를 증가시켜 영향 x
    if data[i] == "<":
        i += 1
        while data[i] != ">":
            i += 1
        i += 1 # 닫힌 괄호 만나면 인덱스 하나 증가 시켜 다음 가르킴
    # 숫자나 알파벳을 만나는 경우
    elif data[i].isalnum():
        start = i
        while i < len(data) and data[i].isalnum():
            i+=1
        # 숫자 알파벳 범위까지 뒤집는다.
        tmp = data[start:i]
        tmp.reverse()
        # 뒤집은 것으로 교체
        data[start:i] = tmp
    # 괄호도 알파벳 숫자도 아니면 증가 (공백)
    else:
        i += 1

print("".join(data))
        
        