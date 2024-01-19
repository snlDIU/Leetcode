class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:

        # Initialize variables
        M = len(matrix)
        N = len(matrix[0])
        prevRow = matrix[0][:]

        # Iterate through rows starting from the second row (r = 1)
        for r in range(1, M):
            currRow = [0] * N  # Initialize the current row
            
            # Iterate through columns
            for c in range(N):
                curr = matrix[r][c]
                
                # Calculate the three possible paths: top, top-left, top-right
                top = curr + prevRow[c]
                topL = curr + prevRow[c - 1] if c > 0 else float('inf')
                topR = curr + prevRow[c + 1] if c < N - 1 else float('inf')
                
                # Choose the minimum path and update the current row
                currRow[c] = min(top, topL, topR)
            
            prevRow = currRow  # Update the previous row with the current row

        # Return the minimum falling path sum
        return min(prevRow)

        