# p 365
import heapq
n = int(input())
heap = []
for i in range(n):
  heapq.heappush(heap,int(input()));

result = 0;

while len(heap) != 1:
  # 가장 작은 2개의 카드묶음 꺼내기
  one = heapq.heappop(heap)
  two = heapq.heappop(heap)
  # 카드 묶음을 합쳐서 다시 삽입
  sum_value = one + two
  result += sum_value
  heapq.heappush(heap, sum_value)

print(result)
  