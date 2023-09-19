# 无向图
graph = {"A": ["B", "C"],
         "B": ["A", "C", "D"],
         "C": ["A", "B", "E"],
         "D": ["B", "C", "E", "F"],
         "E": ["C", "D"],
         "F": ["D"]
         }
def bfs(graph,s):
    # 队列，存放节点
    queue=[]
    queue.append(s)
    visited=set()
    visited.add(s)
    while queue:
        vertex=queue.pop(0)
        for node in graph[vertex]:
            if node not in visited:
                queue.append(node)
                visited.add(node)
        print(vertex)
bfs(graph,'A')
#
# def dfs(graph,s):
#     # 队列，存放节点
#     stack=[]
#     stack.append(s)
#     visited=set()
#     visited.add(s)
#     while stack:
#         vertex=stack.pop()
#         for node in graph[vertex]:
#             if node not in visited:
#                 stack.append(node)
#                 visited.add(node)
#         print(vertex)
# dfs(graph,"E")

# dijkstra
# graph = {"A": {"B": 5, "C": 1},
#          "B": {"A": 5, "C": 2, "D": 1},
#          "C": {"A": 1, "B": 2, "D": 4, "E": 8},
#          "D": {"B": 1, "C": 4, "E": 3, "F": 6},
#          "E": {"C": 8, "D": 3},
#          "F": {"D": 6}
#          }
# import heapq
# import math
# def dijkstra(graph,s):
#     pqueue=[]
#     heapq.heappush(pqueue,(0,s))
#     seen=set()
#     parent={s:None}
#     distance=init_distance(graph,s)
#     while (len(pqueue)>0):
#         pair=heapq.heapq.heapop(pqueue)
#         dist=pair[0]
#         vertex=pair[1]
#         seen.add(vertex)
#         nodes=graph[vertex].keys()
#         for w in nodes:
#             if w not in seen:
#                 if dist+graph[vertex][w]<distance[w]:
#                     heapq.heappush(pqueue,(dist+graph[vertex][w],w))
#                     parent[w]=vertex
#                     distance[w]=dist+graph[vertex][w]
#         return parent