class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        left = ['(', '{', '[']
        right = [')', '}', ']']
        for bracket in s:
            if bracket in left:
                stack.append(bracket)
            else:
                if bracket == ')' and (len(stack) == 0 or stack[-1] != '('):
                    return False
                elif bracket == '}' and (len(stack) == 0 or stack[-1] != '{'):
                    return False
                elif bracket == ']' and (len(stack) == 0 or stack[-1] != '['):
                    return False
                else:
                    stack.pop()
        return False if len(stack) != 0 else True


print(Solution().isValid(']'))
