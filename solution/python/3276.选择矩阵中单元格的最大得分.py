class Solution:
    def maxScore(self, grid: list[list[int]]) -> int:
        rows = len(grid)
        value_rows = {}
        for row, line in enumerate(grid):
            for value in line:
                value_rows.setdefault(value, set()).add(row)

        states = [0] * (1 << rows)
        for value in sorted(value_rows, reverse=True):
            next_states = states[:]
            for mask, score in enumerate(states):
                for row in value_rows[value]:
                    if not mask >> row & 1:
                        next_mask = mask | (1 << row)
                        next_states[next_mask] = max(
                            next_states[next_mask], score + value
                        )
            states = next_states
        return max(states)


if __name__ == "__main__":
    test_cases = [([[1, 2, 3], [4, 3, 2], [1, 1, 1]], 8), ([[8, 7, 6], [8, 3, 2]], 15)]
    for _, (grid, expected) in enumerate(test_cases):
        assert Solution().maxScore(grid) == expected
