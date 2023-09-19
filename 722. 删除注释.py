from typing import List


class Solution:
    def removeComments(self, source: List[str]) -> List[str]:
        res = []
        is_comment = False
        for line in source:
            if not is_comment:
                ans = ''
            i = 0
            while i < len(line):
                if line[i:i + 2] == '/*' and not is_comment:
                    is_comment = True
                    i += 1
                elif line[i:i + 2] == '*/' and is_comment:
                    is_comment = False
                    i += 1
                elif line[i:i + 2] == '//' and not is_comment:
                    break
                elif not is_comment:
                    ans += line[i]
                i += 1
            if ans and not is_comment:
                res.append(ans)
        return res


print(Solution().removeComments(
    ["main() {", "  Node* p;", "  /* declare a Node", "  /*float f = 2.0", "   p->val = f;", "   /**/",
     "   p->val = 1;", "   //*/ cout << success;*/", "}", " "]))
