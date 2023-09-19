# 正向逆向判断
# 用一个变量left保持左括号的数量，一个变量right保存右括号的数量
# class Solution:
#     def longestValidParentheses(self, s: str) -> int:
#         if not s:
#             return 0
#
#         n, left, right, max_len = len(s), 0, 0, 0
#         for i in range(n):
#             if s[i] == '(':
#                 left += 1
#             else:
#                 right += 1
#             if right > left:
#                 left = right = 0
#             elif left == right:
#                 max_len = max(right * 2, max_len)
#         left = right = 0
#         for i in range(n - 1, -1, -1):
#             if s[i] == '(':
#                 left += 1
#             else:
#                 right += 1
#             if left > right:
#                 left = right = 0
#             elif left == right:
#                 max_len = max(right * 2, max_len)
#         return max_len

# dp[i]=dp[i-1]+dp[i-dp[i-1]-2]+2
#dp表示当以i位置的括号为结尾，最长有效括号的个数
# class Solution:
#     def longestValidParentheses(self, s: str) -> int:
#         if not s:
#             return 0
#         dp=[0]*len(s)
#         for i in range(1,len(s)):
#             if s[i]==')' and i-dp[i-1]-1>=0 and s[i-dp[i-1]-1]=='(':
#                 dp[i]=dp[i-1]+dp[i-dp[i-1]-2]+2
#         return max(dp)
# print(Solution().longestValidParentheses("((()))"))

# 使用栈来存放括号的索引
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = [-1]
        length = 0
        max_length = 0
        for i in range(len(s)):
            if s[i] == '(':
                stack.append(i)
            else:
                stack.pop()
                if stack == []:
                    stack.append(i)
                else:
                    length = i-stack[-1]
                    max_length = max(max_length,length)
        return max_length

print(Solution().longestValidParentheses('()'))