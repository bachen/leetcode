# Definition for a binary tree node.
class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {integer[]}
	def preorderTraversal(self, root):
		result = []
		if root == None:
			return result
		else:
			getresult(root,result)
		return result

def getresult(root,result):
	if root == None:
		return result
	else:
		result.append(root.val)
		getresult(root.left,result)
		getresult(root.right,result)
		return result

s0 = TreeNode(7)
s1 = TreeNode(1)
s2 = TreeNode(4)
s3 = TreeNode(2)
s4 = TreeNode(3)
s5 = TreeNode(6)
s6 = TreeNode(8)
s7 = TreeNode(5)
s0.left =s1
s0.right = s2
s1.left = s3
s1.right = s4
s4.left = s6
s2.left = s5
s5.right = s7
test = Solution()
print test.preorderTraversal(s0)