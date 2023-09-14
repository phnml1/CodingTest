def two_sum(nums, target):
    memo = {}
    # O(n)
    for v in nums:
        memo[v] = 1
    # O(n)
    for v in nums:
        needed_number = target-v
        if needed_number!=v and needed_number in memo:
            return True
    return False
print(two_sum(nums = [1,5,4,6,10],target = 10))