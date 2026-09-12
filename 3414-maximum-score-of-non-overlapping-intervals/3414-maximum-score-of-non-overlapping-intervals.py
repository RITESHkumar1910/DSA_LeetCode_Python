from bisect import bisect_left
from typing import List

class Solution:
    def maximumWeight(self, intervals: List[List[int]]) -> List[int]:
        n = len(intervals)

        # Add original index
        arr = []
        for i, (l, r, w) in enumerate(intervals):
            arr.append((l, r, w, i))

        # Sort by ending point
        arr.sort(key=lambda x: x[1])

        ends = [x[1] for x in arr]

        # dp[k][i] = (maximum score, lexicographically smallest indices)
        # using at most k intervals among first i intervals
        dp = [[(0, ()) for _ in range(n + 1)] for _ in range(5)]

        for k in range(1, 5):
            for i in range(1, n + 1):
                # Option 1: don't take current interval
                best_score, best_indices = dp[k][i - 1]

                l, r, w, idx = arr[i - 1]

                # Find number of previous intervals whose end < current start
                p = bisect_left(ends, l)

                # Option 2: take current interval
                prev_score, prev_indices = dp[k - 1][p]

                take_score = prev_score + w
                take_indices = tuple(sorted(prev_indices + (idx,)))

                # Choose better score
                if take_score > best_score:
                    best_score = take_score
                    best_indices = take_indices

                # Same score -> lexicographically smaller indices
                elif take_score == best_score:
                    if take_indices < best_indices:
                        best_indices = take_indices

                dp[k][i] = (best_score, best_indices)

        return list(dp[4][n][1])