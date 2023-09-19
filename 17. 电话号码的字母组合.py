from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        phone_button = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv',
                        '9': 'wxyz'}
        res=[]
        def dfs(ind,letter):
            if ind==len(digits):
                res.append(letter)
                return
            for ch in phone_button[digits[ind]]:
                dfs(ind+1,letter+ch)
        dfs(0,'')
        if not digits:
            return []
        return res
