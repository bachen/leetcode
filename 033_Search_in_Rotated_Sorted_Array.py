class Solution:
    # @param {integer[]} nums
    # @param {integer} target
    # @return {integer}
    def search(self, nums, target):
        length = len(nums)
        if length == 0:
        	return -1
        if (length == 1):
        	if (nums[0]==target):
        		return 0
        	else:
        		return -1
        mid = length/2
        if nums[mid]== target:
        	return mid
        index = -1
        index = binarysearch(nums,0,mid,target)
        index = binarysearch(nums,mid+1,length-1,target)
        return index

def binarysearch(nums,start,end,target):
    if start == end:
    	return -1
    mid = (end-start+1)/2
    if nums[mid]== target:
        return mid
    binarysearch(nums,start,mid,target)
    binarysearch(nums,mid+1,end,target)

test = Solution()
print test.search([4,5,6,7,0,1,2,3],4)