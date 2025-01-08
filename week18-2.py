# week18-2.py 二合一
#Leetcode 54. Spiral Matrix
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        M, N = len(matrix), len(matrix[0])
        i, j =0, 0
        di = [0, 1, 0 ,-1]
        dj = [1, 0, -1, 0]
        d = 0
        ans = []
        while len(ans) < M*N:
            ans.append( matrix[i][j] )
            matrix[i][j] = 999

            i2, j2 = i + di[d], j + dj[d]
            if i2 >= M or j2 >=N or i2 < 0 or j2 < 0 or matrix[i2][j2]==999:
                d = (d+1) % 4
                i2, j2 = i + di[d], j + dj[d]
            i, j = i2, j2
        return ans
