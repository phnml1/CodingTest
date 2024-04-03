nums = [1,2,3,4];

def solution(nums):
  result = []
  def backtrack(start,curr,k):
    if len(curr) == k:
      result.append(curr[:]);
      return;
    for i in range(start,len(nums)):
      curr.append(nums[i]);
      backtrack(i+1,curr,k);
      curr.pop();
  for i in range(len(nums)+1):
    backtrack(0,[],i);
  return result;
print(solution(nums));
      