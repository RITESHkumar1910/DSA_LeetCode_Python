class Solution:
    def hasValidPath(self, grid):
        m = len(grid)
        n = len(grid[0])

        # Total path length must be even
        if (m + n - 1) % 2 != 0:
            return False

        # Starting cell must be '('
        if grid[0][0] == ')':
            return False

        dp = [set() for _ in range(n)]
        dp[0].add(1)

        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    continue

                cur = set()

                # From above
                if i > 0:
                    cur.update(dp[j])

                # From left
                if j > 0:
                    cur.update(dp[j - 1])

                value = 1 if grid[i][j] == '(' else -1

                dp[j] = {
                    balance + value
                    for balance in cur
                    if balance + value >= 0
                }

        return 0 in dp[n - 1]