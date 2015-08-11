class Solution:
    # @param {integer[]} nums
    # @param {integer} target
    # @return {boolean}
    def search(self, nums, target):
        length = len(nums)
        if length == 0:
        	return False
        if length == 1:
        	if nums[0] == target:
        		return True
        	else:
        		return False
        pivot = None
        for i in range(1,length):
        	if (nums[i] - nums[i-1]) < 0:
        		pivot = i
        if pivot:
        	return (binarysearch(nums[:pivot],target) | binarysearch(nums[pivot:],target))
        else:
        	return binarysearch(nums,target)

def binarysearch(nums,target):
    length = len(nums)
    if length == 1:
        if nums[0] == target:
        	return True
        else:
        	return False
    mid = length/2
    if (target < nums[0]) | (target > nums[-1]):
    	return False
    if (nums[mid] > target):
    	return binarysearch(nums[:mid],target)    
    elif nums[mid] == target:
    	return True
    else:
    	return binarysearch(nums[mid:],target)	

test = Solution()
print test.search([5,7,1,2,4,5],5)