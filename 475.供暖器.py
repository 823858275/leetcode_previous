#
# @lc app=leetcode.cn id=475 lang=python3
#
# [475] 供暖器
#
class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        n=len(heaters)  #列表heaters的长度
        res=0           #最终结果，初始化为0
        heaters.sort()  #对列表heaters进行排序
        for h in houses:#遍历列表houses中每个元素，进行二分排序，target为h，在heaters中寻找第一个不小于target的元素
            l,r=0,n                      # 二
            while l<r:                  
                mid=l+(r-l)//2           # 分
                if heaters[mid]<h:       # 遍
                    l=mid+1
                else:
                    r=mid                # 历 
            if r==n:        #分别判断r的边界条件情况
                res=max(res,abs(heaters[r-1]-h))
            elif r==0:
                res=max(res,abs(heaters[r]-h))
            else:           #一般情况
                res=max(res,min(abs(heaters[r-1]-h),abs(heaters[r]-h)))
        return res
            

