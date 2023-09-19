#快排
#partion函数实现将数组从left到right部分，选择一个基准点，将大于基准点的数放到基准点后面，小于基准点的数放到基准点前面
def partion(nums,left,right):
    #选取基准点
    key=nums[right]
    #慢指针i的位置（存放小于key的数）
    i=left-1
    #快指针j遍历整个数组，找到小于key的数之后交换i，j的数
    for j in range(left,right):
        if nums[j]<=key:
            i+=1
            nums[i],nums[j]=nums[j],nums[i]
    nums[i+1],nums[right]=nums[right],nums[i+1]
    return i+1
def quickSort(nums,left,right):
    if left<right:
        q=partion(nums,left,right)
        quickSort(nums,left,q-1)
        quickSort(nums,q+1,right)
a=[2,4,1,3,5]
quickSort(a,0,len(a)-1)
print(a)

