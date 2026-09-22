class Solution:
    def resultArray(self, nums, k, queries):
        n = len(nums)

        tree = [[0] * k for _ in range(4 * n)]
        prod = [1] * (4 * n)

        def merge(a, b):
            p1, c1 = a
            p2, c2 = b

            p = (p1 * p2) % k
            c = c1[:]

            for r in range(k):
                c[(p1 * r) % k] += c2[r]

            return p, c

        def build(node, l, r):
            if l == r:
                v = nums[l] % k
                prod[node] = v
                tree[node][v] = 1
                return

            mid = (l + r) // 2

            build(node * 2, l, mid)
            build(node * 2 + 1, mid + 1, r)

            prod[node], tree[node] = merge(
                (prod[node * 2], tree[node * 2]),
                (prod[node * 2 + 1], tree[node * 2 + 1])
            )

        def update(node, l, r, idx, val):
            if l == r:
                v = val % k
                prod[node] = v
                tree[node] = [0] * k
                tree[node][v] = 1
                return

            mid = (l + r) // 2

            if idx <= mid:
                update(node * 2, l, mid, idx, val)
            else:
                update(node * 2 + 1, mid + 1, r, idx, val)

            prod[node], tree[node] = merge(
                (prod[node * 2], tree[node * 2]),
                (prod[node * 2 + 1], tree[node * 2 + 1])
            )

        def query(node, l, r, ql, qr):
            if ql <= l and r <= qr:
                return prod[node], tree[node][:]

            mid = (l + r) // 2

            if qr <= mid:
                return query(node * 2, l, mid, ql, qr)

            if ql > mid:
                return query(node * 2 + 1, mid + 1, r, ql, qr)

            left = query(node * 2, l, mid, ql, qr)
            right = query(node * 2 + 1, mid + 1, r, ql, qr)

            return merge(left, right)

        build(1, 0, n - 1)

        ans = []

        for index, value, start, x in queries:
            update(1, 0, n - 1, index, value)

            _, cnt = query(1, 0, n - 1, start, n - 1)

            ans.append(cnt[x])

        return ans