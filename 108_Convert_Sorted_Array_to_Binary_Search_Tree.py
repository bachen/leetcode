# Definition for a binary tree node.
class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution:
    # @param {integer[]} nums
    # @return {TreeNode}
	def sortedArrayToBST(self, nums):
		if nums == []:
			return None
		length = len(nums)
		if length == 1:
			root = TreeNode(nums[0])
			return root
		#nums = nums[::-1]
		if length == 2:
			root = TreeNode(nums[1])
			root.left = TreeNode(nums[0])
			return root
		if length == 3:
			root = TreeNode(nums[1])
			root.left = TreeNode(nums[0])
			root.right = TreeNode(nums[2])
			return root
		root = gettree(nums,0,length - 1)
		return root

def gettree(nums,left,right):
	if left > right:
		return None
	middle = (right + left)/2
	root = TreeNode(nums[middle])
	root.left = gettree(nums,left,middle -1)
	root.right = gettree(nums,middle+1,right)
	return root

def gettree1(nums,root,start1,end1,start2,end2):
	if start1 == end1:
		root.left = TreeNode(nums[start1])
	elif start1 < end1:
		l_middle = (end1 - start1)/2
		root.left = TreeNode(nums[l_middle])
		gettree(nums,root.left,start1,l_middle -1,l_middle + 1,end1)
	if start2 == end2:
		root.right = TreeNode(nums[start2])
	elif start2 < end2:
		r_middle = (end2 + start2)/2
		root.right = TreeNode(nums[r_middle])
		gettree(nums,root.right,start2,r_middle - 1,r_middle + 1,end2)
	return None

test = Solution()
s0 = [-99,-98,-97,-96,-94,-93,-91,-90,-88,-87,-86,-85,-83,-81,-80,-79,-78,-76,-73,-72,-70,-69,-66,-65,-64,-63,-61,-59,-57,-56,-55,-54,-53,-52,-51,-48,-45,-44,-43,-42,-41,-40,-39,-37,-34,-33,-32,-31,-30,-28,-26,-24,-22,-20,-19,-18,-16,-15,-14,-12,-10,-9,-8,-6,-5,-4,-3,-2,-1,0,1,2,5,7,8,9,10,11,15,16,17,19,20,21,23,24,26,27,28,30,33,35,36,38,49,50,51,52,54,55,56,57,58,59,60,61,64,65,67,69,70,71,72,73,74,77,79,81,82,85,86,87,88,90,91,94,95,96,97,99]
s1 = [-1,0,1,2]
s3 = [-10,-3,0,5,9,10,11]
print test.sortedArrayToBST(s3).val

'''
	def sortedArrayToBST1(self, nums):
		if nums == []:
			return None
		length = len(nums)
		if length == 1:
			root = TreeNode(nums[0])
			return root
		#nums = nums[::-1]
		if length == 2:
			root = TreeNode(nums[0])
			root.left = TreeNode(nums[1])
			return root
		root = TreeNode(nums[0])
		root.left = TreeNode(nums[1])
		root.right = TreeNode(nums[2])
		old_nodelist = []
		new_nodelist = [root]
		row = 1
		left = length - 3
		if left == 0:
			return root
		i = 3
		count = 2
		while (i < length):
			old_nodelist = new_nodelist
			new_nodelist = []
			if left > 2**row:
				for j in range(2**row):
					new_nodelist.append(TreeNode(i))
					i += 1
				left = left - 2**row
				count = 2**row
			else:
				for j in range(left):
					new_nodelist.append(TreeNode(i))
					i += 1
				count = left
			j = 0
			for node in old_nodelist:
				if j > count - 1:
					break
				node.left = new_nodelist[j]
				j += 1
				if j > count - 1:
					break
				node.right = new_nodelist[j]
				j += 1
		return root

'''