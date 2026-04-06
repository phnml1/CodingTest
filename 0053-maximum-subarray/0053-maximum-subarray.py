class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        DP = [0 for _ in range(len(nums))];
        DP[0] = nums[0];
        for i in range(1,len(nums)):
            DP[i] = max(nums[i],DP[i-1] + nums[i]);
        return max(DP);