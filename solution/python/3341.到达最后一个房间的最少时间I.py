import heapq


class Solution:
    def minTimeToReach(self, moveTime: list[list[int]]) -> int:
        rows, columns = len(moveTime), len(moveTime[0])
        distance = [[float("inf")] * columns for _ in range(rows)]
        distance[0][0] = 0
        queue = [(0, 0, 0)]
        directions = ((1, 0), (-1, 0), (0, 1), (0, -1))
        while queue:
            time, row, column = heapq.heappop(queue)
            if time != distance[row][column]:
                continue
            if row == rows - 1 and column == columns - 1:
                return time
            for row_delta, column_delta in directions:
                next_row, next_column = row + row_delta, column + column_delta
                if 0 <= next_row < rows and 0 <= next_column < columns:
                    arrival = max(time, moveTime[next_row][next_column]) + 1
                    if arrival < distance[next_row][next_column]:
                        distance[next_row][next_column] = arrival
                        heapq.heappush(queue, (arrival, next_row, next_column))
        return -1


if __name__ == "__main__":
    test_cases = [
        (([[0, 4], [4, 4]],), 6),
        (([[0, 0, 0], [0, 0, 0]],), 3),
        (([[0, 1], [1, 2]],), 3),
    ]
    for _, ((move_time,), expected) in enumerate(test_cases):
        assert Solution().minTimeToReach(move_time) == expected
