from typing import List


# i用于从头遍历数组，j用于指向nums应该更新的位置，count表示当前元素已经重复几次
# 当前后不等的时候说明i已经遍历了相同的一段元素，此时j直接存放元素即可
# 前后相等时当count>2说明要直接跳过
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        j, count = 1, 1
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                count = 1
                nums[j] = nums[i]
                j += 1
            else:
                count += 1
                if count <= 2:
                    nums[j] = nums[i]
                    j += 1
        return j


print(Solution().removeDuplicates([1, 1, 1, 2, 2, 3]))
