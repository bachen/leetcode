class Solution:
    # @param {integer[]} nums
    # @return {integer[]}
    def singleNumber(self, nums):
		length = len(nums)
		if length == 0:
			return None
		if length == 2:
			return nums
		x = 0
		for i in nums:
			x = x^i
		print x
		mark = 1
		while ((mark & x) == 0):
			mark = mark << 1
		print mark
		xora = 0
		xorb = 0
		for i in nums:
			if (i & mark) == 0:
				xora = xora^i
			else:
				xorb = xorb^i
		res = []
		res.append(xora)
		res.append(xorb)
		return res

test = Solution()
print test.singleNumber([1,2,3,2,1,5])