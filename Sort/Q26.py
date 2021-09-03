import heapq

n = int(input())

# 힙에 초기 카드 묶음을 모두 삽입
heap = []
for i in range(n):
    data = int(input())
    heapq.heappush(heap, data)

result = 0
# 힙에 원소가 하나 남을 때 까지
while len(heap) != 1:
    a = heapq.heappop(heap)
    b = heapq.heappop(heap)
    heapq.heappush(heap, a+b)
    result += a+b

print(result)