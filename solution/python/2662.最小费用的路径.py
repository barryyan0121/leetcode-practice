"""2662. 最小费用的路径"""

import heapq


class Solution:
    def minimumCost(
        self, start: list[int], target: list[int], specialRoads: list[list[int]]
    ) -> int:
        heap = [(0, *start)]
        best = {tuple(start): 0}
        while heap:
            distance, x, y = heapq.heappop(heap)
            distance = best[(x, y)]
            if [x, y] == target:
                return distance
            candidate = distance + abs(target[0] - x) + abs(target[1] - y)
            if candidate < best.get(tuple(target), 10**18):
                best[tuple(target)] = candidate
                heapq.heappush(heap, (candidate, *target))
            for x1, y1, x2, y2, cost in specialRoads:
                candidate = distance + abs(x1 - x) + abs(y1 - y) + cost
                key = (x2, y2)
                if candidate < best.get(key, 10**18):
                    best[key] = candidate
                    heapq.heappush(heap, (candidate, x2, y2))
        return abs(target[0] - start[0]) + abs(target[1] - start[1])


if __name__ == "__main__":
    assert (
        Solution().minimumCost([1, 1], [4, 5], [[1, 2, 3, 3, 2], [3, 4, 4, 5, 1]]) == 5
    )
