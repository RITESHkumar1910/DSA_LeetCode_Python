class Solution:
    def findKthSmallest(self, coins, k):
        n = len(coins)

        def count(x):
            ans = 0

            # Inclusion-Exclusion
            for mask in range(1, 1 << n):
                L = 1
                bits = 0

                for i in range(n):
                    if mask & (1 << i):
                        bits += 1

                        # LCM
                        g = gcd(L, coins[i])
                        L = L // g * coins[i]

                        if L > x:
                            break

                if L > x:
                    continue

                ways = x // L

                if bits % 2 == 1:
                    ans += ways
                else:
                    ans -= ways

            return ans

        low = 1
        high = min(coins) * k

        # Binary Search
        while low < high:
            mid = (low + high) // 2

            if count(mid) >= k:
                high = mid
            else:
                low = mid + 1

        return low