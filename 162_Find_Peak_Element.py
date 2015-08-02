class Solution:
    # @param nums, an integer[]
    # @return an integer
    def findPeakElement(self, nums):
        length = len(nums)
        if length == 1:
        	return 0
        pre_flag = 0 #initial
        for i in range(1,length):
        	if nums[i] > nums[i-1]:
        		pre_flag = 1
        	if nums[i] < nums[i-1]:
        		if pre_flag == 1:
        			return i-1
        		else:
        			continue
        if pre_flag == 0:
        	return 0
        else:
        	return length-1

test=Solution()
print test.findPeakElement([5,4,3,2])
