class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        unique_paths = [[0 for _ in range(n)] for _ in range(m)]
        for x in range(m):
            unique_paths[x][0] = 1
        for y in range(n):
            unique_paths[0][y] = 1
        
        for x in range(1,m):
            for y in range(1,n):
                unique_paths[x][y] = unique_paths[x-1][y] + unique_paths[x][y-1]

        return unique_paths[m-1][n-1]
        