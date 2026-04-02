class Solution:
    def isPalindrome(self, s: str) -> bool:
        i = 0
        j = len(s) - 1
        
        while i < j:  # Changed from i != j
            # Skip non-alphanumeric from left
            if not s[i].isalnum():
                i += 1
                continue
            # Skip non-alphanumeric from right  
            if not s[j].isalnum():
                j -= 1
                continue
            
            # Compare characters (case-insensitive)
            if s[i].lower() != s[j].lower():  # Added .lower()
                return False
            
            i += 1
            j -= 1
            
        return True