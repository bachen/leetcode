num1 = [1,4,4]
num2 = []
num3 = [1,2,3,4,5]
num4 = [1,1,1,1,1]
num5 = [1,5,6,7]
num6 = [2,3,1,2,7,3]
num7 = [4,5,6]

s1 = 4
s2 = 100
s3 = 11
s4 = 5
s5 = 8
s6 = 7
s7 = 7

class Solution:
    # @param {integer} s
    # @param {integer[]} nums
    # @return {integer}
	def minSubArrayLen(self, s, nums):
		size = len(nums)
		start, end, sum = 0, 0, 0
		bestAns = size + 1
		while end < size:
			while end < size and sum < s:
				sum += nums[end]
				end += 1
			while start < end and sum >= s:
				if sum >= s:
					bestAns = min(bestAns, end - start)
				sum -= nums[start]
				start += 1
		return [0, bestAns][bestAns <= size]

test = Solution()
print test.minSubArrayLen(s1,num1)
print test.minSubArrayLen(s2,num2)
print test.minSubArrayLen(s3,num3)
print test.minSubArrayLen(s4,num4)
print test.minSubArrayLen(s5,num5)
print test.minSubArrayLen(s6,num6)
print test.minSubArrayLen(s7,num7)