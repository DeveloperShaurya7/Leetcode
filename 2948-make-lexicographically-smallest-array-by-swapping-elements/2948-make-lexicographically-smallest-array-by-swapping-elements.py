class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:

        n = len(nums)

        # Sort values along with their original indices
        arr = sorted((value, i) for i, value in enumerate(nums))

        result = nums[:]

        left = 0

        while left < n:
            right = left

            # Find one connected component
            while right + 1 < n and arr[right + 1][0] - arr[right][0] <= limit:
                right += 1

            # Indices belonging to this component
            indices = sorted(arr[k][1] for k in range(left, right + 1))

            # Values in this component are already sorted
            values = [arr[k][0] for k in range(left, right + 1)]

            # Put smallest values at smallest indices
            for idx, value in zip(indices, values):
                result[idx] = value

            left = right + 1

        return result  