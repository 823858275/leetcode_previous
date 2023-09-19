class Solution(object):
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        nums = "".join(sorted(map(str, nums), key=cmp_to_key(lambda x, y: ((x + y) < (y + x)) - ((x + y) > (y + x)))))
        return nums if nums[0] != '0' else '0'
