class Solution:
    # @param {integer[]} nums
    # @return {integer[]}
    def productExceptSelf(self, nums):
    	length = len(nums)
        output = [1]*length
        left = 1
        for i in range(length-1):
        	left *= nums[i]
        	output[i+1] *= left
        right = 1
        for i in xrange(length-1,0,-1):
        	right *= nums[i]
        	output[i-1] *= right
        return output

test = Solution()
print test.productExceptSelf([1,2,3,4])