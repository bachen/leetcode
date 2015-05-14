class Solution:
	def addTwoNumbers(self,l1,l2):
		if (l1 == None) & (l2 == None):
			return None
		if l1 == None:
			return l2
		if l2 == None:
			return l1
		a1 = []
		a2 = []
		cur1 = l1
		cur2 = l2
		while cur1:
			a1.append(cur1.val)
			cur1 = cur1.next
		while cur2:
			a2.append(cur2.val)
			cur2 = cur2.next
		
		a1 = a1[::-1]
		a2 = a2[::-1]
		print a1,a2
		
		result = []
		flag = 0
		while True:
			if a1 == []:
				if (a2 == []) & (flag == 0):
					break
				elif (a2 == []) & (flag == 1):
					result.append(flag)
					break
				else:
					add_sum = a2.pop() + flag
					if add_sum > 9:
						add_sum = add_sum % 10
						result.append(add_sum)
						flag = 1
					else:
						result.append(add_sum)
						flag = 0
			elif a2 == []:
				if a1 == []:
					break
				elif (a1 == []) & (flag == 1):
					result.append(flag)
					break
				else:
					add_sum = a1.pop() + flag
					if add_sum > 9:
						add_sum = add_sum % 10
						result.append(add_sum)
						flag = 1
					else:
						result.append(add_sum)
						flag = 0
			else:
				tmp1 = a1.pop()
				tmp2 = a2.pop()
				add_sum = tmp1 + tmp2 + flag
				if add_sum > 9:
					add_sum = add_sum % 10
					result.append(add_sum)
					flag = 1
				else:
					result.append(add_sum)
					flag = 0
		node = []
		length = len(result)

		for i in range(length):
			print result[i]
			node.append(ListNode(result[i]))

		for i in range(length):
			if i == length-1:
				node[i].next = None
			else:
				node[i].next = node[i+1]
		return node[0]

class ListNode:
	def __init__(self, x):
		self.val = x
		self.next = None

test = Solution()
s1 = ListNode(5)	
t1 = ListNode(5)

s2 = ListNode(7)
s3 = ListNode(0)
s4 = ListNode(3)
s5 = ListNode(6)
s6 = ListNode(7)
s7 = ListNode(3)
s8 = ListNode(2)
s9 = ListNode(1)
s0 = ListNode(5)

t2 = ListNode(9)
t3 = ListNode(2)
t4 = ListNode(5)
t5 = ListNode(5)
t6 = ListNode(6)
t7 = ListNode(1)
t8 = ListNode(2)
t9 = ListNode(2)
t0 = ListNode(4)

s2.next =s3
s3.next =s4
s4.next =s5
s5.next =s6
s6.next =s7
s7.next =s8
s8.next =s9
s9.next =s0

t2.next =t3
t3.next =t4
t4.next =t5
t5.next =t6
t6.next =t7
t7.next =t8
t8.next =t9
t9.next =t0

ss0 = ListNode(2)
ss1 = ListNode(5)
ss0.next = ss1

tt0 = ListNode(5)

test.addTwoNumbers(s1,t1)
test.addTwoNumbers(s2,t2)
test.addTwoNumbers(ss0,tt0)