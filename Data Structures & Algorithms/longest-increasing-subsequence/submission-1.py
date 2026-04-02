class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return 0

        # stack holds tuples: (last_index, subsequence)
        stack = [(i, [nums[i]]) for i in range(len(nums))]
        result = 1

        while stack:
            idx, seq = stack.pop()
            for j in range(idx+1, len(nums)):
                if nums[j] > seq[-1]:
                    new_seq = seq + [nums[j]]
                    result = max(result, len(new_seq))
                    stack.append((j, new_seq))

        return result
