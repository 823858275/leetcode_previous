# def partition(nums, left, right):
#     poivt = nums[left]
#     start = left
#     end = right
#     while start < end:
#         while start < end and nums[end] >= poivt:
#             end -= 1
#         nums[start] = nums[end]
#         while start < end and nums[start] < poivt:
#             start += 1
#         nums[end] = nums[start]
#     nums[start] = poivt
#     return start
#
# print(partition([3, 2, 1, 5, 6, 4],0,5))
print(int("0001"))