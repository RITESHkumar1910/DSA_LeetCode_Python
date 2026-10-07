class Solution:
    def removeInvalidParentheses(self, s):
        # Find minimum number of '(' and ')' to remove
        left = right = 0

        for ch in s:
            if ch == '(':
                left += 1
            elif ch == ')':
                if left > 0:
                    left -= 1
                else:
                    right += 1

        ans = set()

        def dfs(i, left_count, right_count, left_rem, right_rem, path):
            if i == len(s):
                if left_rem == 0 and right_rem == 0:
                    ans.add("".join(path))
                return

            ch = s[i]

            # Option 1: remove current parenthesis
            if ch == '(' and left_rem > 0:
                dfs(i + 1, left_count, right_count,
                    left_rem - 1, right_rem, path)

            elif ch == ')' and right_rem > 0:
                dfs(i + 1, left_count, right_count,
                    left_rem, right_rem - 1, path)

            # Option 2: keep current character
            if ch not in "()":
                path.append(ch)
                dfs(i + 1, left_count, right_count,
                    left_rem, right_rem, path)
                path.pop()

            elif ch == '(':
                path.append(ch)
                dfs(i + 1, left_count + 1, right_count,
                    left_rem, right_rem, path)
                path.pop()

            elif ch == ')' and right_count < left_count:
                path.append(ch)
                dfs(i + 1, left_count, right_count + 1,
                    left_rem, right_rem, path)
                path.pop()

        dfs(0, 0, 0, left, right, [])
        return list(ans)