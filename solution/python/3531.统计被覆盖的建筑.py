from collections import defaultdict


class Solution:
    def countCoveredBuildings(self, n: int, buildings: list[list[int]]) -> int:
        rows = defaultdict(list)
        columns = defaultdict(list)
        for x, y in buildings:
            rows[y].append(x)
            columns[x].append(y)
        row_bounds = {key: (min(values), max(values)) for key, values in rows.items()}
        column_bounds = {
            key: (min(values), max(values)) for key, values in columns.items()
        }
        return sum(
            row_bounds[y][0] < x < row_bounds[y][1]
            and column_bounds[x][0] < y < column_bounds[x][1]
            for x, y in buildings
        )


if __name__ == "__main__":
    test_cases = [
        ((3, [[1, 2], [2, 2], [3, 2], [2, 1], [2, 3]]), 1),
        ((3, [[1, 1], [1, 2], [2, 1], [2, 2]]), 0),
        ((5, [[1, 3], [3, 2], [3, 3], [3, 5], [5, 3]]), 1),
    ]
    for _, ((n, buildings), expected) in enumerate(test_cases):
        assert Solution().countCoveredBuildings(n, buildings) == expected
