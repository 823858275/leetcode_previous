class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        def dfs(ind, step, num1, num2, num3):
            if ind == len(num):
                return
            if step == 0:
                if ind == len(num) - 2:
                    if dfs(ind + 1, step + 1, num1, int(num[ind]), 0):
                        return True
                elif ind == len(num) - 1:
                    return
                else:
                    for i in range(2):
                        if i == 0:
                            if dfs(ind + 1, step, num1 * 10 + int(num[ind]), 0, 0):
                                return True
                        else:
                            if dfs(ind + 1, step + 1, num1, int(num[ind]), 0):
                                return True
            elif step == 1:
                if ind == len(num) - 1:
                    if num1 + num2 == num[ind]:
                        return True
                    else:
                        return
                else:
                    for i in range(2):
                        if i == 0:
                            if dfs(ind + 1, step, num1, num2 * 10 + int(num[ind]), 0):
                                return True
                        else:
                            if dfs(ind + 1, step + 1, num1, num2, int(num[ind])):
                                return True
            else:
                if ind == len(num) - 1:
                    if num1 + num2 == num3 * 10 + int(num[ind]):
                        return True
                    else:
                        return
                else:
                    if num1 + num2 == num3 * 10 + int(num[ind]):
                        if dfs(ind + 1, 0, 0, 0, 0):
                            return True
                    elif num1 + num2 > num3 * 10 + int(num[ind]):
                        if dfs(ind + 1, step, num1, num2, num3 * 10 + int(num[ind])):
                            return True
                    else:
                        return

        return dfs(0, 0, int(num[0]), 0, 0)


print(Solution().isAdditiveNumber("112358"))
