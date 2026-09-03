class Solution:
    def uniformArray(self, nums1):
        mn = min(nums1)

        # If minimum is odd, all elements can be made odd
        if mn % 2 == 1:
            return True

        # Minimum is even, so all elements must already be even
        for x in nums1:
            if x % 2 == 1:
                return False

        return True