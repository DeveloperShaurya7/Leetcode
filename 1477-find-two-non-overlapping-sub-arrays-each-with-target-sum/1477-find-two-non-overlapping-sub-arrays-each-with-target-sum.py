class Solution:
    def minSumOfLengths(self, arr: list[int], target: int) -> int:
        n = len(arr)

        best = [float('inf')] * n

        left = 0
        total = 0

        min_length = float('inf')
        answer = float('inf')

        for right in range(n):
            total += arr[right]

            # Shrink the window
            while total > target:
                total -= arr[left]
                left += 1

            # Found a subarray with sum == target
            if total == target:
                current_length = right - left + 1

                # Find a previous non-overlapping subarray
                if left > 0:
                    answer = min(
                        answer,
                        current_length + best[left - 1]
                    )

                # Store the shortest subarray found so far
                min_length = min(min_length, current_length)

            best[right] = min_length

        return -1 if answer == float('inf') else answer