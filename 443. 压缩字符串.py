from typing import List

# write表示要在char哪个位置写入字符
# i从头到尾遍历 count计数 重复的字符
class Solution:
    def compress(self, chars: List[str]) -> int:
        write = count = 0
        for i, c in enumerate(chars):
            count += 1
            if i + 1 == len(chars) or chars[i + 1] != c:
                chars[write] = c
                if count > 1:
                    write += 1
                    for c in str(count):
                        chars[write] = c
                        write += 1
                else:
                    write += 1
                count = 0
        return write


a = ["a","a","b","b","c","c","c"]
print(a[:Solution().compress(a)])
