class Solution:
    def lexPalindromicPermutation(self, s: str, target: str) -> str:
        n = len(s)

        # Count characters in s
        cnt = [0] * 26
        for ch in s:
            cnt[ord(ch) - ord('a')] += 1

        # Check whether a palindrome is possible
        odd = 0
        middle = ""

        for i in range(26):
            if cnt[i] % 2:
                odd += 1
                middle = chr(ord('a') + i)

        if odd > 1:
            return ""

        # Characters used in the left half
        half_cnt = [x // 2 for x in cnt]
        m = n // 2

        target_half = target[:m]

        # ---------------------------------------------------------
        # 1. Check if target's left half can be formed exactly
        # ---------------------------------------------------------
        rem = half_cnt[:]
        possible = True

        for ch in target_half:
            idx = ord(ch) - ord('a')
            if rem[idx] == 0:
                possible = False
                break
            rem[idx] -= 1

        # If we can form target_half, check the complete palindrome
        if possible:
            left = target_half
            candidate = left + middle + left[::-1]

            if candidate > target:
                return candidate

        # ---------------------------------------------------------
        # 2. Find the smallest left half strictly greater
        #    than target_half
        # ---------------------------------------------------------

        # prefix_count = characters used by target_half[:i]
        prefix_count = [0] * 26

        for i in range(m - 1, -1, -1):

            # We need target_half[:i] to be possible.
            # Build remaining counts after using that prefix.
            rem = half_cnt[:]

            valid_prefix = True

            for j in range(i):
                idx = ord(target_half[j]) - ord('a')

                if rem[idx] == 0:
                    valid_prefix = False
                    break

                rem[idx] -= 1

            if not valid_prefix:
                continue

            # At position i, choose the smallest character
            # greater than target_half[i]
            current = ord(target_half[i]) - ord('a')

            for c in range(current + 1, 26):
                if rem[c] > 0:

                    rem[c] -= 1

                    # Complete the remaining part in sorted order
                    suffix = []

                    for k in range(26):
                        suffix.append(
                            chr(ord('a') + k) * rem[k]
                        )

                    left = (
                        target_half[:i]
                        + chr(ord('a') + c)
                        + ''.join(suffix)
                    )

                    candidate = left + middle + left[::-1]

                    if candidate > target:
                        return candidate

                    rem[c] += 1

        return ""