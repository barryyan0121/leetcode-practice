from typing import List


class Solution:
    def getMinDistance(self, nums: List[int], target: int, start: int) -> int:
        return min(
            abs(index - start) for index, value in enumerate(nums) if value == target
        )


if __name__ == "__main__":
    solution = Solution()
    assert solution.getMinDistance([1, 2, 3, 4, 5], 5, 3) == 1
    print("1848 passed")
