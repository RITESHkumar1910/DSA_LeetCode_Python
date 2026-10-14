class Solution:
    def maxSumOfSquares(self, num: int, sum: int) -> str:
        if sum > 9 * num:
            return ""

        digits = [0] * num
        remaining = sum

        for i in range(num):
            digits[i] = min(9, remaining)
            remaining -= digits[i]

        if remaining > 0:
            return ""

        return ''.join(map(str, digits))