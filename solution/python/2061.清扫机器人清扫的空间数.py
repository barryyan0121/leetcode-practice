"""2061. 清扫机器人清扫的空间数"""


class Solution:
    def numberOfCleanRooms(self, room: list[list[int]]) -> int:
        rows, cols = len(room), len(room[0])
        directions = ((0, 1), (1, 0), (0, -1), (-1, 0))
        row = col = direction = cleaned = 0
        visited = set()
        while (row, col, direction) not in visited:
            visited.add((row, col, direction))
            if room[row][col] == 0:
                room[row][col] = 2
                cleaned += 1
            nr, nc = row + directions[direction][0], col + directions[direction][1]
            if not (0 <= nr < rows and 0 <= nc < cols) or room[nr][nc] == 1:
                direction = (direction + 1) % 4
            else:
                row, col = nr, nc
        return cleaned


if __name__ == "__main__":
    test_cases = [(([[0, 0], [1, 0]],), 3)]
    for _, (args, expected) in enumerate(test_cases):
        assert Solution().numberOfCleanRooms(*args) == expected
