class Solution:
    def maxPalindromes(self, s: str, k: int) -> int:
        n = len(s)

        dp = [0] * (n + 1)
        pal = [False] * n

        for r in range(n):
            dp[r + 1] = dp[r]

            # IMPORTANT: go from left to right
            for l in range(r + 1):
                if s[l] == s[r] and (r - l <= 1 or pal[l + 1]):
                    pal[l] = True

                    if r - l + 1 >= k:
                        dp[r + 1] = max(dp[r + 1], dp[l] + 1)
                else:
                    pal[l] = False

        return dp[n]