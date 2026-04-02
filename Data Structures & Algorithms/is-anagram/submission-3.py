from collections import defaultdict
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if (len(s) != len(t)):
            return False

        dictionary = defaultdict(int)

        for i in range(len(s)):
            dictionary[s[i]] += 1
            dictionary[t[i]] -= 1
        
        for v in dictionary.values():
            if v != 0:
                return False

        return True 

        