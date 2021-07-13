# sys 라이브러리는 한 줄씩 입력 받는다.

import sys
# 하나의 문자열 데이터 입력받기
# rstrip()은 공백문자(엔터 줄 바꿈)를 제거
input_data = sys.stdin.readline().rstrip()

# 입력받은 문자열 그대로 출력
print(input_data)