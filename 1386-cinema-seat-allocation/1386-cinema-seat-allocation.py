class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        rowMask = {}
        
        for row, seat in reservedSeats:
            if 2 <= seat <= 9:
                rowMask[row] = rowMask.get(row, 0) | (1 << (seat - 2))
        
        leftMask  = 0b00001111  # seats 2-5
        midMask   = 0b00111100  # seats 4-7
        rightMask = 0b11110000  # seats 6-9
        
        totalGroups = 0
        
        for mask in rowMask.values():
            leftFree  = (mask & leftMask) == 0
            rightFree = (mask & rightMask) == 0
            
            if leftFree and rightFree:
                totalGroups += 2
            elif leftFree or rightFree or (mask & midMask) == 0:
                totalGroups += 1
        
        emptyRows = n - len(rowMask)
        totalGroups += emptyRows * 2
        
        return totalGroups