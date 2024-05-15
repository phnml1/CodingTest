from collections import defaultdict;
def solution(nums):
    answer = 0;
    count = len(nums)//2;
    nums = list(set(nums));
    
    for k in nums:
        count -= 1;
        answer += 1;
        if count == 0:
            break;
    return answer;
            
    