class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        p1, p2 = 0, 0
        m, n = len(version1), len(version2)
        while p1 < m or p2 < n:
            part1, p1 = self.get_trunk(version1, p1)
            part2, p2 = self.get_trunk(version2, p2)
            if part1!=part2:
                return 1 if part1>part2 else -1
        return 0
    def get_trunk(self, version, p):
        n = len(version)
        if p >= n:
            return 0, p
        else:
            res = ''
            while p <= n-1 and version[p] != '.':
                res += version[p]
                p += 1
            return int(res), p + 1
print(Solution().compareVersion('1','1.1'))