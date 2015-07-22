# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param {TreeNode} root
    # @param {TreeNode} p
    # @param {TreeNode} q
    # @return {TreeNode}
	def lowestCommonAncestor(self, root, p, q):
		node = checktree(root,p.val,q.val)
		return node

def checktree(node,p,q):
	#print node.val
	if node == None:
		return None
	if :
		#print node.val + 'right'
		return checktree(node.right,p,q)
	if ((node.val > p) & (node.val > q)):
		#print node.val + 'left'
		return checktree(node.left,p,q)
	return node

s0 = TreeNode(6)
s1 = TreeNode(5)
s2 = TreeNode(2)
s3 = TreeNode(8)
s4 = TreeNode(3)
s5 = TreeNode(4)
s6 = TreeNode(9)

s0.right = s1

test = Solution()
print test.lowestCommonAncestor(s0,s0,s1).val