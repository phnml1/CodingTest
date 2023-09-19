#중요문제!
def longestConsective(nums):
    longest = 0
    nums_dict = {}
    #O(n)
    for num in nums:
        nums_dict[num] = True # (or num+1)
    # num_set = set(nums);
    for num in nums_dict:
        # O(1)
        if num-1 not in nums_dict:
            cnt = 1
            target = num + 1
            # O(1)
            while target in nums_dict:
                target += 1
                cnt += 1
            longest = max(longest,cnt);
    return longest

print(longestConsective([13,14,1,2,3,7,10,12]))