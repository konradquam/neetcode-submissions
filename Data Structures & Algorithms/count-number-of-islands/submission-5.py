class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        islands = 0
        def bfs(grid, x, y, pattern):
            visited = set()
            queue = deque()
            queue.append((x,y))
            while queue:
                x_ind, y_ind = queue.popleft()
                if grid[x_ind][y_ind] == pattern:
                    grid[x_ind][y_ind] = '#'
                if x_ind > 0 and grid[x_ind-1][y_ind] == pattern:
                    if (x_ind -1, y_ind) not in visited:
                        visited.add((x_ind -1, y_ind))
                        queue.append((x_ind-1, y_ind))
                if x_ind < len(grid) -1 and grid[x_ind +1][y_ind] == pattern:
                    if (x_ind +1, y_ind) not in visited:
                        visited.add((x_ind +1, y_ind))
                        queue.append((x_ind+1, y_ind))
                if y_ind >0 and grid[x_ind][y_ind-1] == pattern:
                    if (x_ind, y_ind -1) not in visited:
                        visited.add((x_ind, y_ind -1))
                        queue.append((x_ind, y_ind-1))
                if y_ind < len(grid[0]) -1 and grid[x_ind][y_ind+1] == pattern:
                    if (x_ind,y_ind+1) not in visited:
                        visited.add((x_ind,y_ind+1) )
                        queue.append((x_ind, y_ind+1))
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    islands +=1
                    bfs(grid, i, j, '1')
            
        return islands

        