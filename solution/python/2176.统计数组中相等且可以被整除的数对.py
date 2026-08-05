"""2176. 统计数组中相等且可以被整除的数对"""


class Solution:
    def countPairs(self, nums: list[int], k: int) -> int:
        return sum(
            nums[i] == nums[j] and i * j % k == 0
            for i in range(len(nums))
            for j in range(i + 1, len(nums))
        )


if __name__ == "__main__":
    test_cases = [(([3, 1, 2, 2, 2, 1, 3], 2), 4)]
    for _, (args, expected) in enumerate(test_cases):
        assert Solution().countPairs(*args) == expected
