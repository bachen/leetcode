# Definition for singly-linked list.
class ListNode:
	def __init__(self, x):
		self.val = x
		self.next = None

class Solution:
    # @param head, a ListNode
    # @return a boolean
	def hasCycle(self, head):
		if head == None:
			return False
		if head.next == None:
			return False
		tmp = head.next 
		if tmp.next == None:
			return False
		fast_p = tmp.next
		slow_p = head
		flag = True
		while True:
			try:
				if slow_p != fast_p:
					tmp = slow_p
					slow_p = tmp.next
					tmp = fast_p.next
					fast_p = tmp.next
				elif slow_p == fast_p:
					flag = True
					break
			except:
				flag = False
				break
		return flag

s=[]
for i in range(5):
	s.append(ListNode(i))
s[0].next = s[1]
s[1].next = s[2]
s[2].next = s[3]
test = Solution()
print test.hasCycle(s[0])
'''
快慢指针：
1. 检查单链表中是否存在循环；
2. 查找倒数第m个node的值。
'''