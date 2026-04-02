class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        result = []
        stack = [([], [False] * n)]   # (current_perm, used_flags)

        while stack:
            curr, used = stack.pop()

            if len(curr) == n:
                result.append(curr)
                continue

            for i in range(n):
                if not used[i]:
                    new_used = used.copy()
                    new_used[i] = True
                    stack.append((curr + [nums[i]], new_used))

        return result
