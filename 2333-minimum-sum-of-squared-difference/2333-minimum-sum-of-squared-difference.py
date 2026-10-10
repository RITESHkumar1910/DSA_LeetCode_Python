class Solution:
    def minSumSquareDiff(self, nums1, nums2, k1, k2):
        diff = [abs(a - b) for a, b in zip(nums1, nums2)]
        k = k1 + k2

        if sum(diff) <= k:
            return 0

        diff.sort(reverse=True)
        diff.append(0)

        for i in range(len(diff) - 1):
            gap = diff[i] - diff[i + 1]
            cost = gap * (i + 1)

            if k >= cost:
                k -= cost
                diff[i] = diff[i + 1]
            else:
                level = diff[i] - k // (i + 1)
                extra = k % (i + 1)

                ans = 0
                for j in range(i + 1):
                    value = level if j >= extra else level - 1
                    ans += value * value

                for j in range(i + 1, len(diff) - 1):
                    ans += diff[j] * diff[j]

                return ans

        return 0