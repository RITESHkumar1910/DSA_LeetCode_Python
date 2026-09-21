class Solution:
    def resultArray(self, nums, k):
        dp = [0] * k
        ans = [0] * k

        for num in nums:
            ndp = [0] * k

            # Start a new subarray
            ndp[num % k] += 1

            # Extend previous subarrays
            for r in range(k):
                if dp[r]:
                    new_r = (r * (num % k)) % k
                    ndp[new_r] += dp[r]

            dp = ndp

            # Add subarrays ending at current index
            for r in range(k):
                ans[r] += dp[r]

        return ans