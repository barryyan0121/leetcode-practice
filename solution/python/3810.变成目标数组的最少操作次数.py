from typing import List


class Solution:
    def minOperations(self, nums: List[int], target: List[int]) -> int:
        return len({value for value, expected in zip(nums, target) if value != expected})


if __name__ == "__main__":
    s = Solution()
    assert s.minOperations([1, 2, 3], [2, 1, 3]) == 2
    assert s.minOperations([4, 1, 4], [5, 1, 4]) == 1
    assert s.minOperations([7, 3, 7], [5, 5, 9]) == 2
