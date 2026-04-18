class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        letter_freq = defaultdict(int)
        max_freq = -1

        result = -1

        left = 0
        for right in range(len(s)):

                letter_freq[s[right]] += 1
                max_freq = max(max_freq, letter_freq[s[right]])

                # replacements = window_len - max_freq
                while (right - left + 1) - max_freq > k:

                        letter_freq[s[left]] -= 1
                        left += 1
                
                result = max(result, right - left + 1)

        return result
