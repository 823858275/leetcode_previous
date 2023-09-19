#
# @lc app=leetcode.cn id=207 lang=python3
#
# [207] 课程表
#
# 判断有向图是否有环
class Solution:  # 拓扑排序，有向图如果有环则无法被拓扑排序那么接下来看看拓扑排序的经典算法：选择入度为0的节点输出，从有向图中删除此节点以及出边，循环上述过程，直到有向图中无节点或无入度为0的节点，循环结束
    # 即选择图中入度为0结点，删除并将下一个结点入度-1
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        if numCourses == 0:
            return True
        in_degrees = [0 for _ in range(numCourses)]  # 先构建图，in_degree记录结点的入度
        adj = [set() for _ in range(numCourses)]  # adj记录每个结点的下一个结点（用集合表示）
        for first, second in prerequisites:
            in_degrees[first] += 1
            adj[second].add(first)
        queue = []  # 队列存放入度为0的结点
        for i in range(numCourses):
            if in_degrees[i] == 0:
                queue.append(i)
        count = 0
        while queue:  # 整个过程遍历所有的结点
            top = queue.pop(0)  # 删除该节点
            count += 1
            for next_num in adj[top]:
                in_degrees[next_num] -= 1  # 当前节点的下一个节点入度-1
                if in_degrees[next_num] == 0:  # 如果入度为0则加入队列
                    queue.append(next_num)
        return count == numCourses  # 判读是否遍历完所有节点
