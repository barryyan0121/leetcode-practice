"""3568. 清理教室的最少移动"""

from collections import deque


class Solution:
    def minMoves(self, classroom: list[str], energy: int) -> int:
        lumetarkon = classroom
        rows, cols = len(classroom), len(classroom[0])
        trash = {}
        start = 0
        for i, row in enumerate(classroom):
            for j, value in enumerate(row):
                position = i * cols + j
                if value == "S":
                    start = position
                elif value == "L":
                    trash[position] = len(trash)
        target_mask = (1 << len(trash)) - 1
        if target_mask == 0:
            return 0

        states = 1 << len(trash)
        best = [[-1] * (rows * cols) for _ in range(states)]
        best[0][start] = energy
        queue = deque([(start, 0, energy, 0)])
        while queue:
            position, mask, remaining, moves = queue.popleft()
            if mask == target_mask:
                return moves
            row, col = divmod(position, cols)
            current = classroom[row][col]
            if remaining == 0 and current == "R":
                remaining = energy
            for nr, nc in (
                (row - 1, col),
                (row + 1, col),
                (row, col - 1),
                (row, col + 1),
            ):
                if not (0 <= nr < rows and 0 <= nc < cols):
                    continue
                if classroom[nr][nc] == "X":
                    continue
                next_energy = remaining - 1
                if next_energy < 0:
                    continue
                next_position = nr * cols + nc
                next_mask = mask
                if next_position in trash:
                    next_mask |= 1 << trash[next_position]
                if classroom[nr][nc] == "R":
                    next_energy = energy
                if next_energy > best[next_mask][next_position]:
                    best[next_mask][next_position] = next_energy
                    queue.append((next_position, next_mask, next_energy, moves + 1))
        return -1


if __name__ == "__main__":
    test_cases = [
        ((["S.", "XL"], 2), 2),
        ((["LS", "RL"], 4), 3),
        ((["L.S", "RXL"], 3), -1),
    ]
    for _, ((classroom, energy), expected) in enumerate(test_cases):
        assert Solution().minMoves(classroom, energy) == expected
