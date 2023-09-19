# 在一个数组中，每一个数左边比当前数小的数累加起来，叫做这个数组的小和。求一个数组的小和。
# 例子：
# [1,3,4,2,5]
# 1左边比1小的数，没有；
# 3左边比3小的数，1；
# 4左边比4小的数，1、3；
# 2左边比2小的数，1；
# 5左边比5小的数，1、3、4、2；
# 所以小和为1+1+3+1+1+3+4+2=16
# 要求时间复杂度O(NlogN)，空间复杂度O(N)

# 使用归并排序 getSmallSum算出小和的结果
# merge中计算两个数组之间存在的小和
def merge(nums, left, mid, right):


def getSmallSum(nums, left, right):
    if left == right:
        return 0
    mid = (left + right) // 2
    left_res = getSmallSum(nums, left, mid)
    right_res = getSmallSum(nums, mid + 1, right)
    c = merge(nums, left, mid, right)
    return c + left_res + right_res
