import heapq;
# def solution(food_times, k):
#     answer = 0
#     count = 0
#     while count < k:
#         if answer == len(food_times):
#             answer = 0;
#         if food_times[answer]>0:
#             food_times[answer] -= 1;
#         else:
#             answer += 1;
#             food_times[answer] -= 1;
#         count += 1;
#         answer += 1;
#     count = 0;
#     if answer == len(food_times):
#         answer = 0;
#     while food_times[answer] == 0:
#         count += 1;
#         if count == len(food_times):
#             return -1;
#         if answer == len(food_times):
#             answer = 0;
#         answer += 1;
#     if len(food_times) == answer:
#         return 1;
#     else:
#         answer += 1;
#     return answer

def solution (food_times, k):
  # 전체 음식을 먹는 시간 보다 k가 크거나 같다면
  if sum(food_times) <= k:
    return -1
  q = []
  for i in range(len(food_times)):
    heapq.heappush(q, (food_times[i],i+1));
  sum_value = 0
  previous = 0;
  length = len(food_times);
  
  # sum_value + (현재의 음식 시간 - 이전 음식 시간) * 현재 음식개수와 k 비교
  while sum_value + ((q[0][0] - previous)*length) <= k:
    now = heapq.heappop(q)[0]
    sum_value += (now - previous) * length
    length -= 1;
    previous = now;
  result = sorted(q, key = lambda x : x[1])
  #k에서 몇번째음식을 먹어야하는지
  return result[(k-sum_value) % length][1];
k = int(input())
food_times = list(map(int,input().split()))
print(solution(food_times,k));
print(food_times);