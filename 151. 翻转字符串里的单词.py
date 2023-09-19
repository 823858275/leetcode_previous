class Solution:
    def reverseWords(self, s: str) -> str:
        reversed_string = s.split()
        reversed_string.reverse()
        return " ".join(reversed_string)
