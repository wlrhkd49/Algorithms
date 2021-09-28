
def hanoi_tower(n, start, end):
    if n == 1:
        print(start, end)
        return

    # 막대 번호 1,2,3 이므로 총 6
    # 3개의 막대만 있으므로 가능
    # 6 - start - end = 번호 모를 막대 번호 
    hanoi_tower(n-1, start, 6-start-end)
    print(start, end)
    hanoi_tower(n-1, 6-start-end, end)

n = int(input())
print(2**n-1) # 총 이동 횟수
hanoi_tower(n, 1, 3)