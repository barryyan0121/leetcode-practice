from functools import reduce
from operator import and_, or_


class Solution:
    def minOrAfterOperations(self, nums: list[int], k: int) -> int:
        total_or = reduce(or_, nums)
        total_and = reduce(and_, nums)
        mask = 0

        def can_exclude(candidate: int) -> bool:
            if total_and & candidate:
                return False
            current = (1 << 30) - 1
            groups = 0
            for number in nums:
                current &= number
                if not (current & candidate):
                    groups += 1
                    current = (1 << 30) - 1
            return len(nums) - groups <= k

        for bit in range(29, -1, -1):
            candidate = mask | (1 << bit)
            if can_exclude(candidate):
                mask = candidate
        return total_or & ~mask


if __name__ == "__main__":
    test_cases = [
        (([3, 5, 3, 2, 7], 2), 3),
        (([7, 3, 15, 14, 2, 8], 4), 2),
        (([10, 7, 10, 3, 9, 14, 9, 4], 1), 15),
    ]
    for _, ((nums, k), expected) in enumerate(test_cases):
        assert Solution().minOrAfterOperations(nums, k) == expected
