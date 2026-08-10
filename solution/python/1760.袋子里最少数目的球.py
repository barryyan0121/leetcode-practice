from typing import List


class Solution:
    def minimumSize(self, nums: List[int], maxOperations: int) -> int:
        left, right = 1, max(nums)
        while left < right:
            mid = (left + right) // 2
            operations = sum((value - 1) // mid for value in nums)
            if operations <= maxOperations:
                right = mid
            else:
                left = mid + 1
        return left


if __name__ == "__main__":
    solution = Solution()
    assert solution.minimumSize([9], 2) == 3
    assert solution.minimumSize([2, 4, 8, 2], 4) == 2
    print("1760 passed")
