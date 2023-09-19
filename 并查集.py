"""
一个对象即整个并查集的树
用字典father记录每个节点的父节点，key为节点的值，value为它的父节点
find 查找x的祖宗节点，然后把x的所有父节点的父节点设置祖宗节点，路径压缩
merge 合并两个节点，如果x y的根节点不等，则合并为同一个根节点
is_connected 判断两个节点是否连通，即判断两个节点是否有同一个根节点
add 添加新节点
"""
class UnionFind:
    def __init__(self):
        """
        记录每个节点的父节点
        """
        self.father = {}

    def find(self, x):
        """
        查找根节点
        路径压缩
        """
        root = x

        while self.father[root] != None:
            root = self.father[root]

        # 路径压缩
        while x != root:
            original_father = self.father[x]
            self.father[x] = root
            x = original_father

        return root

    def merge(self, x, y, val):
        """
        合并两个节点
        """
        root_x, root_y = self.find(x), self.find(y)

        if root_x != root_y:
            self.father[root_x] = root_y

    def is_connected(self, x, y):
        """
        判断两节点是否相连
        """
        return self.find(x) == self.find(y)

    def add(self, x):
        """
        添加新节点
        """
        if x not in self.father:
            self.father[x] = None
