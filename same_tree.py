# Definition for a binary tree node.
class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution:
	# @param {TreeNode} p
	# @param {TreeNode} q
	# @return {boolean}
	def isSameTree(self, p, q):
		if (p == None) & (q == None):
			#print "(p == None) & (q == None)"
			return True
		elif ((p != None) & (q == None)) | ((p == None) & (q != None)):
			#print "((p != None) & (q == None)) | ((p == None) & (q != None))"
			return False
		elif p.val != q.val:
			return False
		else:
			left = self.isSameTree(p.left,q.left)
			right = self.isSameTree(p.right,q.right)
			return left & right

tree1 = []
treenode1 = [1,3,7]
for i in treenode1:
	tree1.append(TreeNode(i))
tree1[0].right = tree1[2]
tree1[0].left = tree1[1]



tree2 = []
treenode2 = [1,3,7]
for i in treenode2:
	tree2.append(TreeNode(i))
tree2[0].left = tree2[1]
tree2[1].right = tree2[2]

test = Solution()
print test.isSameTree(tree1[0],tree2[0])