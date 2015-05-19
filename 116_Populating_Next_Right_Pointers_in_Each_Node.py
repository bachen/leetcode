# Definition for binary tree with next pointer.
class TreeLinkNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None
		self.next = None

class Solution:
    # @param root, a tree link node
    # @return nothing
	def connect(self, root):
		if root == None:
			return None
		left_to_right(root.left,root.right)

def left_to_right(left,right):
	pass