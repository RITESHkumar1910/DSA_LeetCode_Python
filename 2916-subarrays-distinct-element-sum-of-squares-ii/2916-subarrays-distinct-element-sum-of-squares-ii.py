class Solution:
    def sumCounts(self, nums: list[int]) -> int:
        MOD = 10**9 + 7
        n = len(nums)

        tree_sum = [0] * (4 * n)
        tree_sq = [0] * (4 * n)
        lazy = [0] * (4 * n)

        def apply(node, l, r, val):
            length = r - l + 1

            tree_sq[node] = (
                tree_sq[node]
                + 2 * val * tree_sum[node]
                + length * val * val
            ) % MOD

            tree_sum[node] = (
                tree_sum[node] + length * val
            ) % MOD

            lazy[node] = (lazy[node] + val) % MOD

        def push(node, l, r):
            if lazy[node] == 0 or l == r:
                return

            mid = (l + r) // 2
            val = lazy[node]

            apply(node * 2, l, mid, val)
            apply(node * 2 + 1, mid + 1, r, val)

            lazy[node] = 0

        def pull(node):
            left = node * 2
            right = left + 1

            tree_sum[node] = (
                tree_sum[left] + tree_sum[right]
            ) % MOD

            tree_sq[node] = (
                tree_sq[left] + tree_sq[right]
            ) % MOD

        def update(node, l, r, ql, qr):
            if ql > r or qr < l:
                return

            if ql <= l and r <= qr:
                apply(node, l, r, 1)
                return

            push(node, l, r)

            mid = (l + r) // 2

            update(node * 2, l, mid, ql, qr)
            update(node * 2 + 1, mid + 1, r, ql, qr)

            pull(node)

        last = {}
        ans = 0

        for i, x in enumerate(nums):
            prev = last.get(x, -1)

            update(1, 0, n - 1, prev + 1, i)

            last[x] = i
            ans = (ans + tree_sq[1]) % MOD

        return ans