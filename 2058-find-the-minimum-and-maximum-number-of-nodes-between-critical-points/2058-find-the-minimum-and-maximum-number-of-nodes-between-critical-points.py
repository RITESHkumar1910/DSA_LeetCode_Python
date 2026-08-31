class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        prev = head
        curr = head.next

        index = 1
        first = -1
        last = -1
        minDist = float('inf')

        while curr and curr.next:
            # Check whether current node is a critical point
            is_max = curr.val > prev.val and curr.val > curr.next.val
            is_min = curr.val < prev.val and curr.val < curr.next.val

            if is_max or is_min:
                if first == -1:
                    # First critical point
                    first = index
                else:
                    # Distance from previous critical point
                    minDist = min(minDist, index - last)

                last = index

            prev = curr
            curr = curr.next
            index += 1

        # Fewer than two critical points
        if first == -1 or first == last:
            return [-1, -1]

        # Maximum distance
        maxDist = last - first

        return [minDist, maxDist]