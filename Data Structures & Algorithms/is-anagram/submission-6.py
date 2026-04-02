class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if not s or not t:
            return False

        if len(s) != len(t):
            return False
        
        dictionary = defaultdict(int)

        for i in range(len(s)):
            dictionary[s[i]] += 1
            dictionary[t[i]] -= 1
        
        for i in dictionary:
            if dictionary[i] != 0:
                return False
        
        return True
