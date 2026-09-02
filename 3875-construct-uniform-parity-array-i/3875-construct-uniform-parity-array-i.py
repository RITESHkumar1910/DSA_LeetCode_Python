class Solution:
    def uniformArray(self, nums1):
        # If all numbers already have the same parity
        if all(x % 2 == 0 for x in nums1):
            return True

        if all(x % 2 != 0 for x in nums1):
            return True

       
        return True