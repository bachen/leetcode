# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param two ListNodes
    # @return the intersected ListNode
    def getIntersectionNode(self, headA, headB):
        if (headB == None) | (headA == None):
            return None
        lengthA = 0
        lengthB = 0
        pa = headA
        pb = headB
        while(pa != None):
            lengthA += 1
            pa = pa.next
        while(pb!= None):
            lengthB += 1
            pb = pb.next
        pa = headA
        pb = headB
        if lengthB > lengthA:
            for i in range(lengthB -lengthA):
                pb = pb.next
        else:
            for i in range(lengthA -lengthB):
                pa = pa.next
        print pa.val,pb.val
        for i in range(min(lengthB,lengthA)):
            if pa == pb:
                return pa
            pa = pa.next
            pb = pb.next
        return None

L0 = ListNode(2)
L1 = ListNode(3)
L0.next = L1

test = Solution()
print test.getIntersectionNode(L0,L1).val