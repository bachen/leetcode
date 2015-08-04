class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def rob(self, nums):
        if nums == []:
            return 0
    	length = len(nums)
    	if length < 2:
    		return max(nums)
        res = [nums[0],max(nums[0],nums[1])]
        for i in range(2,length):
        	res.append(max(nums[i]+res[i-2],res[i-1]))
        return res[-1]

test = Solution()
print test.rob([2,0])