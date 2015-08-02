class Solution:
    # @param {integer[]} nums
    # @return {boolean}
    def containsDuplicate(self, nums):
        d = {}
        length = len(nums)
        if length == 0:
            return False
        if length == 1:
            return False
        for i in nums:
            if d.has_key(i):
                return True
            else:
                d[i] = 1
        return False