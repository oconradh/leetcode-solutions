class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        m = len(matrix)
        n = len(matrix[0])
        matrix_t = [[0]*m for i in range(n)]
        
        for i in range(m):
            for j in range(n):
                matrix_t[j][i] = matrix[i][j]
        return matrix_t
