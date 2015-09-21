# Below is the interface for Iterator, which is already defined for you.
#
# class Iterator(object):
#     def __init__(self, nums):
#         """
#         Initializes an iterator object to the beginning of a list.
#         :type nums: List[int]
#         """
#
#     def hasNext(self):
#         """
#         Returns true if the iteration has more elements.
#         :rtype: bool
#         """
#
#     def next(self):
#         """
#         Returns the next element in the iteration.
#         :rtype: int
#         """

class PeekingIterator(object):
    def __init__(self, iterator):
        """
        Initialize your data structure here.
        :type iterator: Iterator
        """
        self.iter = iterator
        self.peeknext = None

    def peek(self):
        """
        Returns the next element in the iteration without advancing the iterator.
        :rtype: int
        """
        if self.peeknext == None:
            self.peeknext = self.iter.next()
        return self.peeknext

    def next(self):
        """
        :rtype: int
        """
        if self.peeknext == None:
            self.peeknext = self.iter.next()
        val = self.peeknext
        self.peeknext = None
        return val

    def hasNext(self):
        """
        :rtype: bool
        """
        if self.peeknext == None:
            return self.iter.hasNext()
        else:
            return True

# Your PeekingIterator object will be instantiated and called as such:
# iter = PeekingIterator(Iterator(nums))
# while iter.hasNext():
#     val = iter.peek()   # Get the next element but not advance the iterator.
#     iter.next()         # Should return the same value as [val].