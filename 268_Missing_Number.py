class Solution(object):
    def missingNumber1(self, nums):
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

    def missingNumber(self, nums): #constant space, linear time
        """
        :type nums: List[int]
        :rtype: int
        """
        max_val = nums[0]
        real = 0
        ideal = 0
        count = 0
        for i in nums:
        	if max_val < i:
        		max_val = i
        	real += i
        	ideal += count
        	count += 1
        res = max_val - (real-ideal)
        if res == max_val:
        	return max_val+1
        else:
        	return res

test = Solution()
print test.missingNumber([0,3,4,2])