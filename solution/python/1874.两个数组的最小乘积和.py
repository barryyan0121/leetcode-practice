from typing import List


class Solution:
    def minProductSum(self, nums1: List[int], nums2: List[int]) -> int:
        return sum(a * b for a, b in zip(sorted(nums1), sorted(nums2, reverse=True)))


if __name__ == "__main__":
    solution = Solution()
    assert solution.minProductSum([5, 3, 4, 2], [4, 2, 2, 5]) == 40
    print("1874 passed")
