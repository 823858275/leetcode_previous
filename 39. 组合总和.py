from typing import List
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res=[]
        def dfs(sum_list,tmp_res,ind):
            if sum_list>target:
                return
            if sum_list==target:
                res.append(tmp_res)
                return
            for i in range(ind,len(candidates)):
                dfs(sum_list+candidates[i],tmp_res+[candidates[i]],i)
        dfs(0,[],0)
        return res