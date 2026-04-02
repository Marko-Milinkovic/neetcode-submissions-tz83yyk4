class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        result = 0
        current_window = set()
        left = 0

        for right in range(len(s)):

            while s[right] in current_window:
                current_window.remove(s[left])
                left += 1

            current_window.add(s[right])
            result = max(result, right - left + 1)

        return result