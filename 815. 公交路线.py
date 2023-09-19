import collections


# 将一条公交线路作为图中的一个节点，如果两个公交线路有交点，则两个节点相邻
# 将节点和深度依次放入队列中，并用seen表示节点已经遍历过，
class Solution(object):
    def numBusesToDestination(self, routes, S, T):
        if S == T:
            return 0
        routes = list(map(set, routes))
        graph = collections.defaultdict(set)
        for i, r1 in enumerate(routes):
            for j in range(i + 1, len(routes)):
                r2 = routes[j]
                for r in r1:
                    if r in r2:
                        graph[i].add(j)
                        graph[j].add(i)

        seen, targets = set(), set()
        for node, route in enumerate(routes):
            if S in route:
                seen.add(node)
            if T in route:
                targets.add(node)

        queue = [(node, 1) for node in seen]
        while queue:
            pair=queue.pop(0)
            node, depth = pair[0],pair[1]
            if node in targets:
                return depth
            for nei in graph[node]:
                if nei not in seen:
                    seen.add(nei)
                    queue.append((nei, depth + 1))
        return -1
print(Solution().numBusesToDestination([[7,12],[4,5,15],[6],[15,19],[9,12,13]],15,12))