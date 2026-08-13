"""3066. 超过阈值的最少操作数 II"""

import heapq


class Solution:
    def minOperations(self, nums: list[int], k: int) -> int:
        heapq.heapify(nums)
        operations = 0
        while len(nums) > 1 and nums[0] < k:
            first = heapq.heappop(nums)
            second = heapq.heappop(nums)
            heapq.heappush(nums, first * 2 + second)
            operations += 1
        return operations


if __name__ == "__main__":
    test_cases = [
        (([2, 11, 10, 1, 3], 10), 2),
        (([1, 1, 2, 4, 9], 20), 4),
    ]
    for _, (args, expected) in enumerate(test_cases):
        assert Solution().minOperations(*args) == expected
