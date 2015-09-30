class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = 0
        for i in nums:
        	if nums[abs(i)] > 0:
        		nums[abs(i)] = -nums[abs(i)]
        	else:
        		res = abs(i)
        		break
        for i in nums:
        	nums[abs(i)] = abs(nums[abs(i)])
        return res

test = Solution()
print test.findDuplicate([4,4,3,1,2,5])