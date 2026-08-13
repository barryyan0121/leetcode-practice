"""3858. 按位或的最小值"""


class Solution:
    def minimumOR(self, grid: list[list[int]]) -> int:
        forbidden = 0
        answer = 0
        max_value = max(max(row) for row in grid)
        for bit in range(max_value.bit_length() - 1, -1, -1):
            trial = forbidden | (1 << bit)
            if all(any((value & trial) == 0 for value in row) for row in grid):
                forbidden = trial
            else:
                answer |= 1 << bit
        return answer


if __name__ == "__main__":
    test_cases = [
        (([[1, 5], [2, 4]],), 3),
        (([[3, 5], [6, 4]],), 5),
        (([[7, 9, 8]],), 7),
    ]
    for _, (args, expected) in enumerate(test_cases):
        assert Solution().minimumOR(*args) == expected
