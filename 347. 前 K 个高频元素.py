from typing import List
import collections
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_dic=collections.Counter(nums)
        res=[]
        for value,freq in freq_dic.items():
            heapq.heappush(res,(freq,value))
            if len(res)>k:
                heapq.heappop(res)
        return [x[1] for x in heapq.nlargest(k,res)]

print(Solution().topKFrequent([1,1,1,2,2,3],2))
