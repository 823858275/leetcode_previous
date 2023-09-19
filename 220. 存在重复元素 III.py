# 数据分桶，桶的大小为t+1
# 假设桶为bucket，对于数组中的某个元素nums[i]，其在桶里的索引为num[i]//bucket_size
# 对于i，首先要将索引距离k的给排除
# 则当前桶内有值则return True，再判断前后一个位置的桶的值是否满足要求
from typing import List
class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        bucket_size=t+1
        bucket={}
        for i in range(len(nums)):
            bucket_index=nums[i]//bucket_size
            if bucket_index in bucket:
                return True
            bucket[bucket_index]=nums[i]
            if bucket.get(bucket_index-1,0) and abs(nums[i]-bucket[bucket_index-1])<=t:
                return True
            if bucket.get(bucket_index+1,0) and abs(nums[i]-bucket[bucket_index+1])<=t:
                return True
            if i-k>=0:
                bucket.pop(nums[i-k]//bucket_size)
        return False

print(Solution().containsNearbyAlmostDuplicate([1,5,9,1,5,9],2,3))