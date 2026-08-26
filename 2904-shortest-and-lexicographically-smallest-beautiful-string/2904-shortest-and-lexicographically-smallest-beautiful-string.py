class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        pos = []

        # Store positions of all 1s
        for i, ch in enumerate(s):
            if ch == '1':
                pos.append(i)

        # Not enough 1s
        if len(pos) < k:
            return ""

        min_len = float('inf')
        ans = ""

        # Check every k consecutive 1s
        for i in range(len(pos) - k + 1):
            l = pos[i]
            r = pos[i + k - 1]

            cur = s[l:r + 1]
            length = r - l + 1

            if length < min_len:
                min_len = length
                ans = cur
            elif length == min_len and cur < ans:
                ans = cur

        return ans