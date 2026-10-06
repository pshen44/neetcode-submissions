class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        N = len(grid)
        M = len(grid[0])
        fresh = 0
        q = deque()
        for i in range(N):
            for j in range(M):
                if grid[i][j] == 2:
                    q.append([i,j])
                elif grid[i][j] == 1:
                    fresh += 1

        res = 0

        while q and fresh > 0:
            res += 1
            for _ in range(len(q)):
                x, y = q.popleft()
                directions = [(0,1), (1,0), (-1,0), (0,-1)]
                for dx, dy in directions:
                    newX = dx + x
                    newY = dy + y
                    if (newX < N and newY < M and
                        newX >= 0 and newY >= 0 and
                        grid[newX][newY] == 1):
                        grid[newX][newY] = 2
                        q.append([newX, newY])
                        fresh -= 1
        return res if fresh == 0 else -1
        