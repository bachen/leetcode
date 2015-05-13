class Solution:
    # @param {integer} s
    # @param {integer[]} nums
    # @return {integer}
    def minSubArrayLen(self, s, nums):
        l=len(nums)
        if (l == 1) & (nums[0] == s):
        	return 1
        else:
        	return 0
        