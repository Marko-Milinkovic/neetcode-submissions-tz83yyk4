class Solution:
    def threeSum(self, nums):
        nums.sort()  # Sort the array
        result = []

        for i in range(len(nums) - 2):
            # Skip duplicate elements for the first number
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            left = i + 1
            right = len(nums) - 1

            while left < right:
                total = nums[i] + nums[left] + nums[right]

                if total < 0:
                    left += 1  # Need a larger number
                elif total > 0:
                    right -= 1  # Need a smaller number
                else:
                    # Found a valid triplet
                    result.append([nums[i], nums[left], nums[right]])

                    # Skip duplicates for second number
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1

                    # Skip duplicates for third number
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1

                    # Move pointers inward
                    left += 1
                    right -= 1

        return result
