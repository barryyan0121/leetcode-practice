from collections import Counter
from typing import List


class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        counts = Counter(nums)
        return sum(value for value, count in counts.items() if count == 1)


if __name__ == "__main__":
    solution = Solution()
    assert solution.sumOfUnique([1, 2, 3, 2]) == 4
    assert solution.sumOfUnique([1, 1, 1, 1, 1]) == 0
    print("1748 passed")
