class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): 
            return False
        
        dictionary = {}
        
        for i in range(len(s)):
            # Initialize keys if they don't exist
            if s[i] not in dictionary:
                dictionary[s[i]] = 0
            if t[i] not in dictionary:
                dictionary[t[i]] = 0
                
            dictionary[s[i]] += 1
            dictionary[t[i]] -= 1
        
        # Check if all counts are zero
        for count in dictionary.values():
            if count != 0:
                return False
                
        return True