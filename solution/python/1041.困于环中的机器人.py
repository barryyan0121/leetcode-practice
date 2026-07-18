from typing import List


class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        row = column = direction = 0
        for instruction in instructions:
            if instruction == "G":
                delta_row, delta_column = directions[direction]
                row += delta_row
                column += delta_column
            elif instruction == "L":
                direction = (direction - 1) % 4
            else:
                direction = (direction + 1) % 4
        return (row, column) == (0, 0) or direction != 0


if __name__ == "__main__":
    solution = Solution()
    test_cases = [("GGLLGG", True), ("GG", False), ("GL", True), ("GLGLGGLGL", False)]
    for _, (instructions, expected) in enumerate(test_cases):
        assert solution.isRobotBounded(instructions) == expected
