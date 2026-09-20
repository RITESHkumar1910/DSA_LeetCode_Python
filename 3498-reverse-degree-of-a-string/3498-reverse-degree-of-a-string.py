class Solution:
    def reverseDegree(self, s: str) -> int:
        ans = 0

        for i, ch in enumerate(s):
            reversed_position = ord('z') - ord(ch) + 1
            string_position = i + 1

            ans += reversed_position * string_position

        return ans