numbers = [1,3,2,6,-1,4,1,8,2]

#최댓값
# 전체에서 앞에서부터 하나씩 빼는 느낌
def maxSlidingWindow(numbers,k):
  window = sum(numbers[:k]); 
  answer = 0
  for i in range(k,len(numbers)):
    window += numbers[i] - numbers[i-k]
    answer = max(answer,window)
  return answer
def minSlidingWindow(numbers,k):
  min_sum = 9999
  window_sum = 0
  start = 0
  for end in range(len(numbers)):
    window_sum += numbers[end];
    if end >= k-1:  
      if window_sum <= min_sum:
        min_sum = window_sum;
      window_sum -= numbers[start]
      start+=1;
  return min_sum;