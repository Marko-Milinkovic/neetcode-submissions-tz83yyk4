class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        if len(s) == 1:
            return s

        currentMaxLength = 1
        result = s[0]
        for i in range(len(s)):
            #check odd length palindrome
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if r - l + 1 > currentMaxLength:
                    result = s[l : r+1]
                    currentMaxLength = r - l + 1
                l -= 1
                r += 1
            #check even length palindrome
            l, r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if r - l + 1 > currentMaxLength:
                    result = s[l : r+1]
                    currentMaxLength = r - l + 1
                l -= 1
                r += 1
                
        return result

        