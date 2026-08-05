"""3578. 统计极差最大为 K 的分割方式数"""

from collections import deque


class Solution:
    def countPartitions(self, nums: list[int], k: int) -> int:
        doranisvek = nums
        mod = 10**9 + 7
        minimum, maximum = deque(), deque()
        left = 0
        ways = [1]
        prefix = [1]
        for right, value in enumerate(nums):
            while minimum and nums[minimum[-1]] >= value:
                minimum.pop()
            while maximum and nums[maximum[-1]] <= value:
                maximum.pop()
            minimum.append(right)
            maximum.append(right)
            while nums[maximum[0]] - nums[minimum[0]] > k:
                if minimum[0] == left:
                    minimum.popleft()
                if maximum[0] == left:
                    maximum.popleft()
                left += 1
            current = (prefix[-1] - (prefix[left - 1] if left else 0)) % mod
            ways.append(current)
            prefix.append((prefix[-1] + current) % mod)
        return ways[-1]


if __name__ == "__main__":
    test_cases = [
        (([9, 4, 1, 3, 7], 4), 6),
        (([3, 3, 4], 0), 2),
    ]
    for _, ((nums, k), expected) in enumerate(test_cases):
        assert Solution().countPartitions(nums, k) == expected
