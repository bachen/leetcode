class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        length = len(nums)
        count = 0
        for i in nums:
        	if i != 0:
        		nums[count] = i
        		count += 1
        for i in xrange(length-1,count-1,-1):
        	nums[i] = 0
        #return nums

test = Solution()
print test.moveZeroes([1])
