"""3342. 到达最后一个房间的最少时间 II"""

import heapq


class Solution:
    def minTimeToReach(self, moveTime: list[list[int]]) -> int:
        rows, columns = len(moveTime), len(moveTime[0])
        distance = [[[float("inf")] * 2 for _ in range(columns)] for _ in range(rows)]
        distance[0][0][0] = 0
        queue = [(0, 0, 0, 0)]
        directions = ((1, 0), (-1, 0), (0, 1), (0, -1))

        while queue:
            time, row, column, parity = heapq.heappop(queue)
            if time != distance[row][column][parity]:
                continue
            if row == rows - 1 and column == columns - 1:
                return time
            cost = 1 if parity == 0 else 2
            next_parity = parity ^ 1
            for row_delta, column_delta in directions:
                next_row, next_column = row + row_delta, column + column_delta
                if 0 <= next_row < rows and 0 <= next_column < columns:
                    arrival = max(time, moveTime[next_row][next_column]) + cost
                    if arrival < distance[next_row][next_column][next_parity]:
                        distance[next_row][next_column][next_parity] = arrival
                        heapq.heappush(
                            queue, (arrival, next_row, next_column, next_parity)
                        )
        return -1


if __name__ == "__main__":
    test_cases = [
        (([[0, 4], [4, 4]],), 7),
        (([[0, 0, 0, 0], [0, 0, 0, 0]],), 6),
        (([[0, 1], [1, 2]],), 4),
    ]
    for _, ((move_time,), expected) in enumerate(test_cases):
        assert Solution().minTimeToReach(move_time) == expected
