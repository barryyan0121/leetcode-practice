from typing import List


class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        return (1 << (len(nums) - 1)) * __import__("functools").reduce(
            lambda a, b: a | b, nums
        )


if __name__ == "__main__":
    solution = Solution()
    assert solution.subsetXORSum([1, 3]) == 6
    print("1863 passed")
