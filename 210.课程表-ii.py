#
# @lc app=leetcode.cn id=210 lang=python3
#
# [210] 课程表 II
#
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        if numCourses==0:
            return []
        in_degree=[0 for _ in range(numCourses)]
        adj=[set() for _ in range(numCourses)]
        for second,first in prerequisites:
            in_degree[second]+=1
            adj[first].add(second)
        queue=[]
        for i in range(numCourses):
            if in_degree[i]==0:
                queue.append(i)
        res=[]
        while queue:
            top=queue.pop(0)
            res.append(top)
            for next_num in adj[top]:
                in_degree[next_num]-=1
                if in_degree[next_num]==0:
                    queue.append(next_num)
        return res if len(res)==numCourses else []





