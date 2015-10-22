class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sum1 = 0
        sum2 = 0
        count = 0
        for i in nums:
            sum1 += i
            sum2 += count
            count += 1
        res = sum1 - sum2
        return res

test = Solution()
print test.findDuplicate([1,1])