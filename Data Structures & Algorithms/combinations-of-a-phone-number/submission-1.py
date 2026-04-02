class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        phone = {
            "2": "abc", "3": "def", "4": "ghi", "5": "jkl",
            "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"
        }

        stack = [("", 0)]  # (current string, index in digits)
        result = []

        while stack:
            combo, i = stack.pop()

            if i == len(digits):  
                result.append(combo)
                continue

            for ch in phone[digits[i]]:
                stack.append((combo + ch, i + 1))

        return result
