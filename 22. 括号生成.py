from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        # n_left表示ans中左括号的个数
        # n_right表示ans中右括号的个数
        # stack_left表示剩余与右括号配对的左括号
        def dfs(n_left, n_right, stack_left, ans):
            if n_right == n and ans[-1] == ')' and n_left == n:
                res.append(ans)
                return
            if ans[-1] == ')' and stack_left == -1:
                return
            if n_left >= n:
                dfs(n_left, n, stack_left, ans + ')' * (n - n_right))
            else:
                for i in range(2):
                    if i == 0:
                        dfs(n_left + 1, n_right, stack_left + 1, ans + '(')
                    else:
                        dfs(n_left, n_right + 1, stack_left - 1, ans + ')')

        dfs(1, 0, 1, '(')
        return res


print(Solution().generateParenthesis(1))
