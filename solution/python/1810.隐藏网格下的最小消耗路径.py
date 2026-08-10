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
