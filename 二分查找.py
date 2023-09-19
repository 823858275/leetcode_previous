# 边界情况left与右的初始位置要与刚开始的时候相对应
# 查找目标值
def get_target(nums, target):
    left, right = 0, len(nums)  # left为序列的开头，right为序列的末尾索引+1
    while left < right:
        mid = left + (right - left) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1  # 下一轮迭代，left与right的位置与初始相同
        else:
            right = mid
    return -1


# 寻找左侧边界
# 查找第一个不小于目标值的数
# 最后left+1=right,再进行一次迭代，left=right
def find_2(nums, target):
    left, right = 0, len(nums)
    while left < right:
        mid = left + (right - left) // 2
        if nums[mid] < target:
            left = mid + 1
        else:
            right = mid
    if nums[right] < target:
        return -1
    return right


# 查找第一个大于目标值的数
def find_3(nums, target):
    left, right = 0, len(nums)
    while left < right:
        mid = left + (right - left) // 2
        if nums[mid] <= target:
            left = mid + 1
        else:
            right = mid
    return right


nums = [0, 2, 5, 6, 8, 12]
print(find_2(nums, target=7))
