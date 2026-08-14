class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0

        maxIsland = 0
        maxRows, maxCols = len(grid), len(grid[0])
        visited = set()

        def bfs(r, c):
            queue = collections.deque()
            visited.add((r, c))
            queue.append((r, c))

            temp_max = 1
            while queue:
                row, col = queue.popleft()
                directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

                for dr, dc in directions:
                    r, c = row + dr, col + dc
                    if (r in range(maxRows) and c in range(maxCols) and grid[r][c] == 1 and (r, c) not in visited):
                        queue.append((r, c))
                        visited.add((r, c))
                        temp_max += 1
            return temp_max


        for r in range(maxRows):
            for c in range(maxCols):
                if grid[r][c] == 1 and (r, c) not in visited:
                    temp_max = bfs(r, c)
                    maxIsland = max(maxIsland, temp_max)
        
        return maxIsland
                