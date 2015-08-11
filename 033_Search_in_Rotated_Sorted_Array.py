class Solution:
    # @param {integer[]} nums
    # @param {integer} target
    # @return {integer}
    def search(self, nums, target):
        length = len(nums)
        if length == 0:
        	return -1
        if length == 1:
        	if nums[0] == target:
        		return 0
        	else:
        		return -1
        pivot = None
        for i in range(1,length):
        	if (nums[i] - nums[i-1]) < 0:
        		pivot = i
        if pivot:
        	tmp1 = binarysearch(nums[:pivot],target,0)
        	tmp2 = binarysearch(nums[pivot:],target,pivot)
        	print tmp1,tmp2
        	if tmp1 != -1:
        		return tmp1
        	elif tmp2 != -1:
        		return tmp2
        	else:
        		return -1
        else:
        	return binarysearch(nums,target,0)

def binarysearch(nums,target,loc):
    length = len(nums)
    if length == 1:
        if nums[0] == target:
        	return loc
        else:
        	return -1
    mid = length/2
    if (target < nums[0]) | (target > nums[-1]):
    	return -1
    if (nums[mid] > target):
    	return binarysearch(nums[:mid],target,loc)    
    else:
    	return binarysearch(nums[mid:],target,mid+loc)	

test = Solution()
print test.search([7,1,2,4,5],4)