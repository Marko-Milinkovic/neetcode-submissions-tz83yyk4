class Solution:
    def partition(self, s: str) -> List[List[str]]:
        
        def is_palindrome(sub):
            return sub == sub[::-1]
        
        n = len(s)
        stack = [([], 0)]
        result = []

        while stack:

            current_partition , i = stack.pop()

            if i == n:
                result.append(current_partition)
                continue
            
            for j in range(i, n):
                substr = s[i:j+1]
                if is_palindrome(substr):
                    stack.append((current_partition + [substr], j + 1))

        return result

