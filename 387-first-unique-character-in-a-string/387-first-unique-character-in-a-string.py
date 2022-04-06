class Solution:
    def firstUniqChar(self, s: str) -> int:
        flag = 0
        if len(s) == 1:
            return 0

        for i in range(len(s)):
            if s.count(s[i]) == 1:
                return i
            elif s.count(s[i]) > 1:
                flag += 1
                if flag == len(s):
                    return -1
            else:
                return i
   