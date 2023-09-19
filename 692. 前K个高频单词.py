from typing import List
import heapq
import collections

# 用哈希表计算words中每个单词的频次
# 再用堆来统计topk个高频单词
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        freq_dic = collections.Counter(words)
        queue = []
        for word, freq in freq_dic.items():
            heapq.heappush(queue, (-freq, word))
        return [heapq.heappop(queue)[1] for _ in range(k)]


print(Solution().topKFrequent(["i", "love", "leetcode", "i", "love", "coding"], 2))
