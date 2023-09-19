from typing import List


class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        if not s:
            return []
        res = []

        def dfs(s, ip, ind):
            if (ind == len(s) and len(ip.strip('.').split('.')) != 4) or len(ip.split('.')) > 4 or int(ip.strip('.').split('.')[-1]) > 255 or (
                    ip.strip('.').split('.')[-1][0] == '0' and len(ip.strip('.').split('.')[-1]) > 1):
                return
            if ind == len(s) and len(ip.strip('.').split('.')) == 4:
                res.append(ip)
                return
            if ip.split('.')[-1] == '0':
                dfs(s, ip + '.', ind)
            elif ip[-1] == '.':
                dfs(s, ip + s[ind], ind + 1)
            else:
                for i in range(2):
                    if i == 0:
                        dfs(s, ip + '.', ind)
                    else:
                        dfs(s, ip + s[ind], ind + 1)

        dfs(s, s[0], 1)
        return res


print(Solution().restoreIpAddresses("0000"))
