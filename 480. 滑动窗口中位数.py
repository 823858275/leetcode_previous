from typing import List
import heapq


# 对顶堆，用一个大顶堆small表示窗口中较小的k//2个数，小顶堆表示窗口中较大的k//2个数，则中位数为small的堆顶或者small和big堆顶之和的一半(由k为奇偶决定)
# 首先对初始窗口进行遍历，将k个数加入small中，然后将small中连续pop出k//2个元素（small中最大的一半元素）
# 然后遍历数组，设置balance为两个堆的初始情况
# 对于窗口最左边的元素left，由于不能在两个堆中直接将left移除，所以用mp[left]记录这个元素待移除

class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        # 对顶堆
        #大顶堆small表示窗口中较小的k // 2个数
        small = []
        #小顶堆big表示窗口中较大的k//2个数
        big = []
        mp = {}
        size = len(nums)
        # 首先对初始窗口进行遍历，将k个数加入small中
        for i in range(k):
            heapq.heappush(small, -nums[i])
        # 然后将small中连续pop出k//2个元素（small中最大的一半元素）
        for i in range(k // 2):
            heapq.heappush(big, -heapq.heappop(small))
        # 中位数为small的堆顶或者small和big堆顶之和的一半(由k为奇偶决定)
        res = []
        if k % 2 == 0:
            res.append((-small[0] + big[0]) / 2)
        else:
            res.append(-small[0])
        #遍历数组
        for i in range(k, size):
            left = nums[i - k]
            # 对于窗口最左边的元素left，由于不能在两个堆中直接将left移除，所以用mp[left]记录这个元素待移除
            mp[left] = mp.get(left, 0) + 1
            # 设置balance为两个堆的初始情况，表示small比big多多少
            balace = 0
            # 如果left>small堆顶元素，说明left在big中，big中要移除left，此时small相对变多，balance+1
            if small and left > -small[0]:
                balace += 1
            # 反之balance-1
            else:
                balace -= 1
            # 对于加入堆中的元素right，如果比small堆顶的元素大，则加入big，balance-1
            if nums[i] > -small[0]:
                balace -= 1
                heapq.heappush(big, nums[i])
            # 反之balance+1
            else:
                balace += 1
                heapq.heappush(small, -nums[i])
            # 经过以上判断，窗口移动后该去除的数去除了，该加的数加入了，现在要调整small和big
            # balance分3种情况，0 1 2
            if balace > 0:
                heapq.heappush(big, -heapq.heappop(small))
            if balace < 0:
                heapq.heappush(small, -heapq.heappop(big))
                balace += 1
            # 后面就是真正处理该移除的数
            while small and mp.get(-small[0], 0) != 0:
                mp[-small[0]] -= 1
                heapq.heappop(small)
            while big and mp.get(big[0], 0) != 0:
                mp[big[0]] -= 1
                heapq.heappop(big)
            # 添加最终结果
            if k % 2 == 0:
                res.append((-small[0] + big[0]) / 2)
            else:
                res.append(-small[0])
        return res


print(Solution().medianSlidingWindow([1, 3, -1, -3, 5, 3, 6, 7], 3))
