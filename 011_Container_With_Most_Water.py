class Solution:
    # @param {integer[]} height
    # @return {integer}
	def maxArea(self, height):
		length = len(height)
		left = 0
		right = length - 1
		base = (right-left)*min(height[left],height[right])
		while (left < right):
			tmp = (right-left)*min(height[left],height[right])
			if tmp > base:
				base = tmp
			if height[left] > height[right]:
				right -= 1
			else:
				left += 1
		return base

test = Solution()
print test.maxArea([2,3,10,5,7,8,9])