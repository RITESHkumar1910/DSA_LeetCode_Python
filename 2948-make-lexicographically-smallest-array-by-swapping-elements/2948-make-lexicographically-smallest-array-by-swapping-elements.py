class Solution:
    def lexicographicallySmallestArray(self, nums, limit):
        n = len(nums)

        # Store (value, original index)
        arr = sorted((value, i) for i, value in enumerate(nums))

        ans = nums[:]
        start = 0

        while start < n:
            end = start

            # Find all values connected by the swap condition
            while end + 1 < n and arr[end + 1][0] - arr[end][0] <= limit:
                end += 1

            # Get original indices of this group
            indices = [arr[i][1] for i in range(start, end + 1)]

            # Smallest values should go to smallest indices
            indices.sort()

            for k, index in enumerate(indices):
                ans[index] = arr[start + k][0]

            start = end + 1

        return ans