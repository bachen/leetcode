class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0
        nums.sort()
        for i in nums:
        	if i != count:
        		return count
        	count += 1
        return count

test = Solution()
print test.missingNumber([0])