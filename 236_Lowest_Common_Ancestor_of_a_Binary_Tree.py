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
    	# bottom - up
        if root == None:
            return None
        print root.val
        if (root == p)|(root == q):
            return root
        L = self.lowestCommonAncestor(root.left, p, q)
        R = self.lowestCommonAncestor(root.right, p, q)
        if (L != None ) & (R != None): #when left & right both return val,means this is the node which is LCA.
            return root
        if L == None:
            return R
        else:
            return L


s0 = TreeNode(6)
s1 = TreeNode(5)
s2 = TreeNode(2)
s3 = TreeNode(8)
s4 = TreeNode(3)
s5 = TreeNode(4)
s6 = TreeNode(9)

s0.right = s1
s0.left = s2
s2.left = s3
s1.left =s4
s4.right = s5
s3.right = s6
test = Solution()
print test.lowestCommonAncestor(s0,s5,s6).val