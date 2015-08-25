class Solution:
    # @param {integer[]} nums
    # @param {integer} k
    # @return {void} Do not return anything, modify nums in-place instead.
    def rotate(self, nums, k):
        length = len(nums)
        while(k > length):
            k = k - length
        res = []
        for i in xrange(-k,length-k,1):
            res.append(nums[i])
        for i in range(length):
            nums[i] = res[i]
        print nums

test = Solution()
test.rotate([1,2,3,5,6,7,8],4)