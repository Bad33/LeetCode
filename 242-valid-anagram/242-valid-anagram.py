class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        str_lst,target = sorted(s),sorted(t)
        s = ''.join([str(item) for item in str_lst])
        t = ''.join([str(item) for item in target])
        if s == t:
            return True
        else:
            return False
        