def TwoSum(nums,target):
    nums.sort();
    l,r = 0, len(nums)-1;
    while l<r:
        if nums[l] + nums[r] < target:
            l+=1
        elif nums[l] + nums[r] > target:
            r-=1
        elif nums[l] + nums[r] == target:
            return True
    return False
print(TwoSum([1,3,4,5,2,9,8],target=4))