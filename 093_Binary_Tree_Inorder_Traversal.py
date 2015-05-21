# Definition for a binary tree node.
class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {integer[]}
	def inorderTraversal(self, root):
		result = []
		if root == None:
			return result
		else:
			getinorder(root,result)
			return result

def getinorder(root,result):
	if root == None:
		return None
	if root.left != None:
		getinorder(root.left,result)
	result.append(root.val)  #中序：左根右
	if root.right != None:
		getinorder(root.right,result)
	return result

test =Solution()
s = []
for i in range(3):
	s.append(TreeNode(i))
s[0].right = s[1]
s[1].left = s[2]
print test.inorderTraversal(s[0])