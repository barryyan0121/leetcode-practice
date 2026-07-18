from functools import cache


class Solution:
    def assignBikes(self, workers: list[list[int]], bikes: list[list[int]]) -> int:
        @cache
        def dfs(worker: int, mask: int) -> int:
            if worker == len(workers):
                return 0
            x, y = workers[worker]
            return min(
                abs(x - bike_x) + abs(y - bike_y) + dfs(worker + 1, mask | (1 << bike))
                for bike, (bike_x, bike_y) in enumerate(bikes)
                if not mask & (1 << bike)
            )

        return dfs(0, 0)


if __name__ == "__main__":
    test_cases = [
        ([[0, 0], [2, 1]], [[1, 2], [3, 3]], 6),
        ([[0, 0], [1, 1], [2, 0]], [[1, 0], [2, 2], [2, 1]], 4),
    ]
    for _, (workers, bikes, expected) in enumerate(test_cases):
        assert Solution().assignBikes(workers, bikes) == expected
