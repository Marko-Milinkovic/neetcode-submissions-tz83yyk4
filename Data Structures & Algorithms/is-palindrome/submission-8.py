class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        l, r = 0, len(s) - 1

        def alphaNum(c):
            return (ord('A') <= ord(c) <= ord('Z') or
                    ord('a') <= ord(c) <= ord('z') or
                    ord('0') <= ord(c) <= ord('9'))

        while l < r:
            
            if not alphaNum(s[l]):
                l += 1
                continue

            if not alphaNum(s[r]):
                r -= 1
                continue

            if s[l].lower() == s[r].lower():
                l += 1
                r -= 1
            else:
                return False
        
        return True




