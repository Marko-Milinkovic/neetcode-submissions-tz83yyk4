class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        result = []
        
        # stack holds: (current_permutation, used_array)
        stack = [([], [False] * n)]

        while stack:
            perm, used = stack.pop()

            if len(perm) == n:
                result.append(perm)
                continue

            for i in range(n):
                if not used[i]:          # O(1) check!
                    new_used = used.copy()
                    new_used[i] = True
                    stack.append((perm + [nums[i]], new_used))

        return result
