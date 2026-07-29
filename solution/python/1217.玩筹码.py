from typing import List


class Solution:
    def minCostToMoveChips(self, position: List[int]) -> int:
        return min(
            sum(value % 2 for value in position),
            sum(value % 2 == 0 for value in position),
        )


if __name__ == "__main__":
    test_cases = [([1, 2, 3], 1), ([2, 2, 2, 3, 3], 2)]
    for _, (position, expected) in enumerate(test_cases):
        assert Solution().minCostToMoveChips(position) == expected
