from collections import Counter
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransom = Counter(ransomNote)
        mag = Counter(magazine)
        
        return all(ransom[c] <= mag[c] for c in string.ascii_lowercase)
 
        