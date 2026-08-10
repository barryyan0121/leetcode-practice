from typing import List


class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        current = 0
        for value in sorted(arr):
            current = min(value, current + 1)
        return current


if __name__ == "__main__":
    solution = Solution()
    assert solution.maximumElementAfterDecrementingAndRearranging([2, 2, 1, 2, 1]) == 2
    print("1846 passed")
