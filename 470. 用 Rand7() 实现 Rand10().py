class Solution:
    def rand10(self):
        """
        :rtype: int
        """
        while True:
            # 0-48
            num = rand7() - 1 + (rand7() - 1) * 7
            if 1 <= num <= 40:
                return num % 10 + 1
            # 1-63
            num = (num % 40) * 7 + rand7()
            if num <= 60:
                return num % 10 + 1
            # 1-21
            num = (num - 61) * 7 + 7
            if num <= 20:
                return num % 10 + 1