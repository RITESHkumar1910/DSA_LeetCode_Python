class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        nums.sort(key=abs)

        n = len(nums)
        ans = 0

        for i in range(n // 2):
            ans -= abs(nums[i]) ** 2

        for i in range(n // 2, n):
            ans += abs(nums[i]) ** 2

        return ans