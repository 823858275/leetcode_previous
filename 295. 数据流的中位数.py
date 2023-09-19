import heapq


# 对顶堆，思路同480
class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.count = 0
        self.small = []
        self.big = []

    def addNum(self, num: int) -> None:
        self.count += 1
        heapq.heappush(self.small, -num)
        heapq.heappush(self.big, -heapq.heappop(self.small))
        if self.count % 2 == 1:
            heapq.heappush(self.small, -heapq.heappop(self.big))

    def findMedian(self) -> float:
        if self.count % 2 == 1:
            return -self.small[0]
        else:
            return (-self.small[0] + self.big[0]) / 2

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
