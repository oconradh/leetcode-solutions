class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        n = len(matrix[0])
        marked_rows = []
        marked_columns = []
        
        for i in range(0,m):
            for j in range(0, n):
                if matrix[i][j] == 0:
                    marked_rows.append(i)
                    marked_columns.append(j)
        
        for i in set(marked_rows):
            matrix[i] = [0] * n
            
        for i in range(0,m):
            for j in set(marked_columns):
                matrix[i][j] = 0
