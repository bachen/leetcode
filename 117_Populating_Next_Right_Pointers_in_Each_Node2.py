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
		if root.left == None:
			return None
		else:
			left = root.left
			right = root.right
			left.next = right
			getresult(root,root.left,root.right)

def getresult(root,left,right):
	if (root != None) & ((left != None) | (right != None)):
		if left != None:
			new_root = left
			new_left = new_root.left
			new_right = new_root.right
			left.next = right
		elif:
			new_root = right
			new_left = new_root.left
			new_right = new_root.right
		while root.next:
			root = root.next
			right.next = root.left
			right = root.right
			left = root.left
			left.next = right
		getresult(new_root,new_left,new_right)
	else:
		return None

s =[]
for i in range(7):
	s.append(TreeLinkNode(i))
s[0].right = s[2]
s[0].left = s[1]
s[1].right = s[4]
s[1].left = s[3]
s[2].right = s[6]
s[2].left = s[5]

test = Solution()
test.connect(s[0])
print s[1].right.val
print s[1].next.val
print s[5].next.val