class Solution:
    # @param {integer[]} nums
    # @return {integer}
	def findMin(self, nums):
		length = len(nums)
		if length == 0:
			return None
		if length == 1:
			return nums[0]
		if length == 2:
			if nums[0] > nums[1]:
				return nums[1]
			else:
				return nums[0]
		if nums[0] < nums[length - 1]:
			return nums[0]
		num = getnum(nums,0,length - 1)
		return num

def getnum(nums,start,end):
	length = end - start + 1
	#print start,end
	if 0 >= length:
		return None
	elif length == 1:
		num = nums[0]
	elif length == 2:
		if nums[start] > nums[end]:
			num = nums[end]
		else:
			num = nums[start]
	else:
		middle = length/2 + start
		#print middle
		num1 = getnum(nums,middle,end)
		num2 = getnum(nums,start,middle)
		if num1 < num2:
			num = num1
		else:
			num = num2
	return num

test = Solution()
print test.findMin([2,3,4,5,1,1])
print test.findMin([6,0,0,1,2,2,3,4])