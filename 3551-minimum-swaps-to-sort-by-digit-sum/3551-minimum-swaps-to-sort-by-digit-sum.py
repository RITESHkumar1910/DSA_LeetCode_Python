class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        def digit_sum(n):
            return sum(int(d) for d in str(n))

        n = len(nums)
        sorted_nums = sorted(nums, key=lambda x: (digit_sum(x), x))

        pos = {num: i for i, num in enumerate(nums)}
        target = [pos[num] for num in sorted_nums]

        visited = [False] * n
        swaps = 0

        for i in range(n):
            if visited[i] or target[i] == i:
                continue

            cycle_size = 0
            j = i

            while not visited[j]:
                visited[j] = True
                j = target[j]
                cycle_size += 1

            swaps += cycle_size - 1

        return swaps