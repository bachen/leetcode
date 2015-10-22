import heapq
class MedianFinder:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.min = []
        self.min_count = 0
        self.max = []
        self.max_count = 0

    def addNum(self, num):
        """
        Adds a num into the data structure.
        :type num: int
        :rtype: void
        """
        if self.min_count == 0:
            heapq.heappush(self.min,-num)
            self.min_count += 1
        elif num < -self.min[0]:
            heapq.heappush(self.min,-num)
            self.min_count += 1
        else:
            heapq.heappush(self.max,num)
            self.max_count += 1
        if (self.min_count - self.max_count) == 2:
            heapq.heappush(self.max,-heapq.heappop(self.min))
            self.min_count -= 1
            self.max_count += 1
        elif (self.max_count - self.min_count) == 2:
            heapq.heappush(self.min,-heapq.heappop(self.max))
            self.min_count += 1
            self.max_count -= 1

    def findMedian(self):
        """
        Returns the median of current data stream
        :rtype: float
        """
        if self.min_count == self.max_count:
            print self.max[0],self.min[0]
            return (self.max[0] - self.min[0])/2.0
        else:
            return -float(self.min[0]) if self.min_count > self.max_count else float(self.max[0])

# Your MedianFinder object will be instantiated and called as such:
# mf = MedianFinder()
# mf.addNum(1)
# mf.findMedian()

m = MedianFinder()
m.addNum(6)
print m.findMedian()
m.addNum(10)
print m.findMedian()
m.addNum(2)
print m.findMedian()