# nums = [1,2,3,4]로 만들 수 있는 모든 순열을 반환하시오
import copy;
nums = [1,2,3,4];

def backtrack(curr):
  
  if len(curr) == len(nums):
    print(curr);
    return;
  for num in nums:
    if num not in curr:
      curr.append(num);
      backtrack(curr);
      curr.pop()
      # or 깊은 복사
    
backtrack([]);