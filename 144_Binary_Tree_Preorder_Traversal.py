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

s =[]
for i in range(3,6):
	s.append(TreeNode(i))
s[0].right = s[1]
s[1].left = s[2]

test = Solution()
print test.preorderTraversal(s[0])