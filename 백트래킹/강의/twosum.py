# def solution(nums,target):
#   n = len(nums)
#   for i in range(n-1):
#     for j in range(i+1,n):
#       if nums[i] + nums[j] == target:
#         return [i,j];
def solution(nums,target):
  def backtrack(start,curr):
    if len(curr) == 2 and sum(curr)==target:
      return curr;
    for i in range(start,len(nums)):
      curr.append(nums[i]);
      ret = backtrack(i+1,curr)
      if ret:
        return ret;
      curr.pop();
    return None;
  return backtrack(0,[]);
print(solution(nums = [4,8,7,5,1],target=12));