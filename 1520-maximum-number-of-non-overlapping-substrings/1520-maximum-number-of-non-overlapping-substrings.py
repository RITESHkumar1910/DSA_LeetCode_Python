class Solution:
    def maxNumOfSubstrings(self, s: str) -> list[str]:
        n = len(s)
        # Step 1: Track first and last occurrences of each character
        l = {}
        r = {}
        for i, ch in enumerate(s):
            if ch not in l:
                l[ch] = i
            r[ch] = i

        intervals = []

        # Step 2: Expand intervals to include all internal characters
        for ch in l:
            left = l[ch]
            right = r[ch]
            valid = True

            j = left
            while j <= right:
                curr_ch = s[j]
                if l[curr_ch] < left:
                    valid = False
                    break
                right = max(right, r[curr_ch])
                j += 1

            if valid:
                intervals.append((right, left))

        # Step 3: Sort intervals by end index for greedy scheduling
        intervals.sort()

        # Step 4: Pick non-overlapping intervals
        result = []
        prev_end = -1

        for right, left in intervals:
            if left > prev_end:
                result.append(s[left : right + 1])
                prev_end = right

        return result