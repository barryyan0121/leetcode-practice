from collections import deque


class Solution:
    def findShortestPath(self, master: "GridMaster") -> int:
        directions = [
            (1, 0, "D", "U"),
            (-1, 0, "U", "D"),
            (0, 1, "R", "L"),
            (0, -1, "L", "R"),
        ]
        open_cells, target = {(0, 0)}, None

        def explore(row, col):
            nonlocal target
            if master.isTarget():
                target = (row, col)
            for dr, dc, move, back in directions:
                nr, nc = row + dr, col + dc
                if (nr, nc) not in open_cells and master.canMove(move):
                    open_cells.add((nr, nc))
                    master.move(move)
                    explore(nr, nc)
                    master.move(back)

        explore(0, 0)
        if target is None:
            return -1
        queue, distance = deque([(0, 0)]), {(0, 0): 0}
        while queue:
            cell = queue.popleft()
            if cell == target:
                return distance[cell]
            for dr, dc, _, _ in directions:
                nxt = (cell[0] + dr, cell[1] + dc)
                if nxt in open_cells and nxt not in distance:
                    distance[nxt] = distance[cell] + 1
                    queue.append(nxt)
        return -1


if __name__ == "__main__":

    class MockGridMaster:
        def __init__(self, grid, target):
            self.grid = grid
            self.pos = (0, 0)
            self.target = target

        def canMove(self, direction):
            drdc = {"D": (1, 0), "U": (-1, 0), "R": (0, 1), "L": (0, -1)}[direction]
            r, c = self.pos[0] + drdc[0], self.pos[1] + drdc[1]
            return (
                0 <= r < len(self.grid)
                and 0 <= c < len(self.grid[0])
                and self.grid[r][c] != 0
            )

        def move(self, direction):
            drdc = {"D": (1, 0), "U": (-1, 0), "R": (0, 1), "L": (0, -1)}[direction]
            self.pos = (self.pos[0] + drdc[0], self.pos[1] + drdc[1])

        def isTarget(self):
            return self.pos == self.target

    grid = [[1, 1, 1], [0, 1, 0], [1, 1, 1]]
    assert Solution().findShortestPath(MockGridMaster(grid, (2, 1))) == 3
