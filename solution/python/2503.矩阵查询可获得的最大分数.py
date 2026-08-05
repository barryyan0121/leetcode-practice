"""2503. 矩阵查询可获得的最大分数"""

import heapq


class Solution:
    def maxPoints(self, grid: list[list[int]], queries: list[int]) -> list[int]:
        rows, columns = len(grid), len(grid[0])
        answer = [0] * len(queries)
        heap = [(grid[0][0], 0, 0)]
        visited = {(0, 0)}
        points = 0
        for query_index, query in sorted(enumerate(queries), key=lambda item: item[1]):
            while heap and heap[0][0] < query:
                _, row, column = heapq.heappop(heap)
                points += 1
                for next_row, next_column in (
                    (row - 1, column),
                    (row + 1, column),
                    (row, column - 1),
                    (row, column + 1),
                ):
                    if (
                        0 <= next_row < rows
                        and 0 <= next_column < columns
                        and (next_row, next_column) not in visited
                    ):
                        visited.add((next_row, next_column))
                        heapq.heappush(
                            heap, (grid[next_row][next_column], next_row, next_column)
                        )
            answer[query_index] = points
        return answer


if __name__ == "__main__":
    test_cases = [(([[1, 2, 3], [2, 5, 7], [3, 5, 1]], [5, 6, 2]), [5, 8, 1])]
    for _, (args, expected) in enumerate(test_cases):
        assert Solution().maxPoints(*args) == expected
