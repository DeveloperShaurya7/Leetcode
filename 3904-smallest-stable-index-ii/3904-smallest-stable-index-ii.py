class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        n = len(nums)

        # Store minimum value from each index to the end
        suffix_min = [0] * n
        suffix_min[n - 1] = nums[n - 1]

        # Build suffix minimum array
        for i in range(n - 2, -1, -1):
            suffix_min[i] = min(nums[i], suffix_min[i + 1])

        # Track maximum value from the left
        prefix_max = float('-inf')

        # Find the first stable index
        for i in range(n):
            prefix_max = max(prefix_max, nums[i])

            if prefix_max - suffix_min[i] <= k:
                return i

        return -1