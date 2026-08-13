from collections import defaultdict
import heapq


class Solution:
    def findShortestPath(self, master: "GridMaster") -> int:
        directions = [
            (1, 0, "D", "U"),
            (-1, 0, "U", "D"),
            (0, 1, "R", "L"),
            (0, -1, "L", "R"),
        ]
        graph = defaultdict(dict)
        target = None

        def explore(row, col):
            nonlocal target
            if master.isTarget():
                target = (row, col)
            for dr, dc, move, back in directions:
                nr, nc = row + dr, col + dc
                if (nr, nc) in graph[row, col]:
                    continue
                if master.canMove(move):
                    cost = master.move(move)
                    graph[row, col][nr, nc] = cost
                    graph[nr, nc][row, col] = cost
                    explore(nr, nc)
                    master.move(back)

        explore(0, 0)
        if target is None:
            return -1
        heap = [(0, 0, 0)]
        distance = {(0, 0): 0}
        while heap:
            cost, row, col = heapq.heappop(heap)
            if (row, col) == target:
                return cost
            if cost != distance[(row, col)]:
                continue
            for (nr, nc), edge in graph[row, col].items():
                new_cost = cost + edge
                if new_cost < distance.get((nr, nc), float("inf")):
                    distance[nr, nc] = new_cost
                    heapq.heappush(heap, (new_cost, nr, nc))
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
            return 0 <= r < len(self.grid) and 0 <= c < len(self.grid[0]) and self.grid[r][c] != 0

        def move(self, direction):
            drdc = {"D": (1, 0), "U": (-1, 0), "R": (0, 1), "L": (0, -1)}[direction]
            self.pos = (self.pos[0] + drdc[0], self.pos[1] + drdc[1])
            return self.grid[self.pos[0]][self.pos[1]]

        def isTarget(self):
            return self.pos == self.target

    grid = [[1, 2], [0, 3]]
    assert Solution().findShortestPath(MockGridMaster(grid, (0, 1))) == 2
